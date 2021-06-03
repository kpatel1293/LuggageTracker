from django.shortcuts import redirect, render
from .models import *  # importing luggage data class
from django.http import JsonResponse
from .blockchain.blockchain import *
from django.contrib.auth.models import User, auth 
from django.contrib import messages #for showing messages either errors or others on html page 

bc = Blockchain()

# get chain
def getChain():
    blockchain = []
    for block in bc.chain:
        blockchain.append(block.__dict__)
    return {"length": len(blockchain), "LuggageBlockchain" : blockchain}

def getLast():
    return getChain()['LuggageBlockchain'][getChain()['length']-1]

def getBlock(index):
    return getChain()['LuggageBlockchain'][index]

# def editBlock(index):
#     getChain()['LuggageBlockchain'][index]['transactions'][0]['origin_airport'] = 'test'
#     print(getChain()['LuggageBlockchain'][index]['transactions'][0]['origin_airport'])

#     return getChain()['LuggageBlockchain'][index]

def checkBlockchain():
    chainLength = bc.getSize()
    try:
        luggageLength = Luggage.objects.count()
    except:
        return False

    if chainLength == 1 and luggageLength == 0:
        return False

    if chainLength == 1 and luggageLength > 0:
        luggageList = Luggage.objects.all()
        for l in luggageList:
            block = { 
                    'tag_id' : l.tag_id,
                    'description' : l.description, 
                    'origin_airport' : l.origin_airport, 
                    # 'transit_airport' : l.transit_airport, 
                    'destination_airport' : l.destination_airport,
                    'status' : l.status,
                    'flag' : l.flagged,
                    'digital_signature' : l.digital_signature
                }

            bc.blockchainTransactions(block)
            bc.mine()
            
            if Blocks.objects.filter(transactions_id = l.tag_id).exists():
                blockUpdate = Blocks.objects.updateBlockchain(Blocks.objects.get(transactions_id = l.tag_id), getLast())
            else:
                addBlock = Blocks.objects.validateBlockchain(getLast(),l)

        print(getChain())
        return True

    return False

try:
    checkBlockchain()
except:
    print('database is not created, comment all functions that are above this line')

# Create your views here. This is include your business logic code to send the data to create the HTML website page
# the request object is from the client and we will be returning something to client webpage
# which the function home() is called in "urls.py"
def home(request):
    return render(request, 'home.html')  # rendering the webpage home to client


#search() called when user submits LuggageTagID on home.html page 
def search(request):
    # Luggage_TagID : str = request.POST["LuggageTagID"] #using POST instead of GET which is more secure 
    try:
        result = Luggage.objects.get(tag_id=request.POST["tag_id"])
        return redirect('result/{}'.format(result))
    except:
        return redirect('notfound') #when Luggage Tag ID not found 


#posting the user search resutls of luggage found from database
def result(request, tag_id):
    if not Luggage.objects.filter(tag_id=tag_id).exists():
        return redirect('notfound')
    context = {'LuggageObject': Luggage.objects.get(tag_id=tag_id), 'Blockchain': Blocks.objects.get(transactions_id=tag_id)}

    return render(request, 'result.html', context)

#for redirects when Luggage Tag ID not found in database 
def notfound(request):
    return render(request, 'notfound.html')

#created new luggage from user input and push to database 
def createLuggage(request):
    try:
        result = Luggage.objects.validateLuggage(request.POST) #push data to database based on user input
        l = Luggage.objects.get(tag_id=result)

        block = { 
            'tag_id' : l.tag_id,
            'description' : l.description, 
            'origin_airport' : l.origin_airport, 
            # 'transit_airport' : l.transit_airport, 
            'destination_airport' : l.destination_airport,
            'status' : l.status,
            'flag' : l.flagged,
            'digital_signature' : l.digital_signature
        }
            
        bc.blockchainTransactions(block)
        bc.mine()

        b = Blocks.objects.validateBlockchain(getLast(),l)

        return redirect('result/{}'.format(result))
    except:
        return redirect('addfailed')

# print(getLast())

#direct to confirmation page of new added luggage
# def addLuggage(request, tag_id):
#     context = {'LuggageObject': Luggage.objects.get(tag_id=tag_id)}
    
#     return render(request, 'addresult.html', context)


#for redirects when new Luggage add or push fails 
def addfailed(request):
    return render(request, 'failedpush.html')

# user clicks on login button takes to login.html page
def movetologin(request):
    return render(request, 'login.html')

# user signin
def login(request):

    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['psw']

        user = auth.authenticate(username=username, password=password) #checking authentication

        if user is not None:
            auth.login(request, user)
            return redirect('/') #home.html
        else:
            messages.error(request, 'Invalid UserName or Password')
            return redirect('movetologin')
        
    return render(request, 'home.html')

# user logout 
def logout(request):
    auth.logout(request)
    return redirect('/') #home.html 

def faq(request):
    return render(request, 'FAQ.html')  # rendering the webpage home to client


def autocomplete(request):
    if 'term' in request.GET:
        qs = Airport.objects.filter(name__icontains=request.GET.get('term'))
        names = list()
        for ap in qs:
            names.append(ap.name)
        # names = [airport.name for ap in qs]
        return JsonResponse(names, safe=False)
    return render(request, 'add.html')