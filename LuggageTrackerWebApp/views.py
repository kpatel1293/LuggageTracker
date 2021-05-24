from django.shortcuts import redirect, render
from .models import *  # importing luggage data class
from django.http import JsonResponse

# Create your views here. This is include your business logic code to send the data to create the HTML website page
# the request object is from the client and we will be returning something to client webpage
# which the function home() is called in "urls.py"
def home(request):
    return render(request, 'home.html')  # rendering the webpage home to client


def result(request, tag_id):
    lug = luggage.objects.all()
    for l in lug:
        if l.tag_id == tag_id:
            context = {'LuggageObject': l}

    return render(request, 'result.html', context)


# search() called when user submits LuggageTagID on home.html page
def search(request):
    # Luggage_TagID : str = request.POST["LuggageTagID"] #using POST instead of GET which is more secure
    try:
        result = luggage.objects.get(tag_id=request.POST["tag_id"])
        return redirect('result/{}'.format(result))
    except:
        return redirect('home')


# add button clicked on homepage takes you to the "add.html" webpage
def movetoadd(request):
    return render(request, 'add.html')


# user submit, adding new Luggage information
def addLuggage(request, tag_id):
    lug = luggage.objects.all()
    for l in lug:
        if l.tag_id == tag_id:
            context = {'LuggageObject': l}

    return render(request, 'addresult.html', context)


def createLuggage(request):
    try:
        result = luggage.objects.validateLuggage(request.POST)
        return redirect('addLuggage/{}'.format(result))
    except:
        return redirect('movetoadd')


# user clicks on login button takes to login.html page
def movetologin(request):
    return render(request, 'login.html')


# user signin
def login(request):
    # code to process sign in
    return render(request, 'home.html')

def faq(request):
    return render(request, 'FAQ.html')  # rendering the webpage home to client


def autocomplete(request):
    if 'term' in request.GET:
        qs = airport.objects.filter(name__icontains=request.GET.get('term'))
        names = []
        for ap in qs:
            names.append(ap.name)
        # names = [airport.name for ap in qs]
        return JsonResponse(names, safe=False)
    return render(request, 'add.html')
