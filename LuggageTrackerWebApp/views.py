from django.shortcuts import render

# Create your views here. This is include your business logic code to send the data to create the HTML website page 

#the request object is from the client and we will be returning something to client webpage 
#which the function home() is called in "urls.py"
def home(request):
    return render(request, 'home.html') #rendering the webpage home to client


#search() called when user submits LuggageTagID
def search(request):

    Luggage_TagID : str = request.POST["LuggageTagID"] #using POST instead of GET which is more secure 

    return render(request, 'result.html', {'result': Luggage_TagID}) #rendering the webpage, sending the result


#add button clicked on homepage takes you to the "add.html" webpage 
def movetoadd(request):
    return render(request, 'add.html') 


#submit, adding new Luggage information 
def addLuggage(request):

    #need to create Luggage object and append all the data submitted from client, as well as, adding to database and blockchain
    #maybe auto generate Tag ID????????????????? 
    #need to store timestamp 
    #return an array of data, need to send it also 

    return render(request, 'addresult.html')