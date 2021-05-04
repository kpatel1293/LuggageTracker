from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here. This is to business logic code to send the data to create the HTML website page 

#the request object is from the client and we will be returning something to client webpage 
#which the function home is called in file "urls.py"
def home(request):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'home.html') #rendering the webpage home

#add fucntion when user clicks on submit 
def add(request):

    val1 = int(request.POST["num1"]) #using POST instead of GET which is more secure 
    val2 = int(request.POST["num2"])

    res = val1 + val2

    return render(request, 'result.html', {'result':res}) #rendering the webpage, sending the added result