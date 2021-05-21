from django.shortcuts import render, redirect
from .models import * #importing luggage data class 
import datetime
from .blockchain_org import *

# Create your views here. This is include your business logic code to send the data to create the HTML website page 

#the request object is from the client and we will be returning something to client webpage 
#which the function home() is called in "urls.py"
def home(request):
    return render(request, 'home.html') #rendering the webpage home to client


#search() called when user submits LuggageTagID on home.html page 
def search(request):

    Luggage_TagID : str = request.POST["LuggageTagID"] #using POST instead of GET which is more secure 

    #needs to retreive luggage information from database, so for now this is dummay data below for demonstration purposes 
    #Luggage1 = luggage()
    #Luggage1.TagID ='ABC12345'
    #Luggage1.Description = 'Samsonite EVOA ICE Blue'
    #Luggage1.TimeStamp = datetime.date.today()
    #Luggage1.Origin_Airport = 'Portland International Airport (PDX)'
    #Luggage1.InTransit_Status = 'Arrived Destination'
    #Luggage1.Destination = 'Chicago O Hare International Airport (ORD)'
    #Luggage1.Current_Location = 'Chicago O Hare International Airport (ORD)'

    #Luggage2 = luggage()
    #Luggage2.TagID = '12345ABC'
    #Luggage1.Description = 'American Tourister LINEX Green'
    #Luggage1.TimeStamp = datetime.date.today()
    #Luggage1.Origin_Airport = 'Los Angeles International Airport (LAX)'
    #Luggage1.InTransit_Status = 'In Transit'
    #Luggage1.Destination = 'John F. Kennedy International Airport (JFK)'
    #Luggage1.Current_Location = 'Seattle-Tacoma International Airport (SEA)'
    
    #Add the luggage objects to array this is dummy data, normally we will be retrieving from database 
    #luggages = [Luggage1, Luggage2]

    #forloop to find the matching user input Luggage TagID 
    #foundLuggage : luggage
    #for L in luggages:
        #if(Luggage_TagID == L.TagID):
            #foundLuggage = L

    
    #instead of using the dummy data above, we will retieve it from database instead, 
    #the dummy data will be added through the admin webpage for now, we will need to change that into user pushing
    #the data to the database 

    luggage_Objects = luggage.objects.all()  #gets all luggage objects in database 
    
    foundLuggage : luggage
    for L in luggage_Objects:
        if(Luggage_TagID == L.tag_id):
            foundLuggage = L

    return render(request, 'result.html', {'LuggageObject': foundLuggage}) #rendering the webpage, sending the result


#add button clicked on homepage takes you to the "add.html" webpage 
def movetoadd(request):
    return render(request, 'add.html') 


#user submit, adding new Luggage information 
def addLuggage(request):

    #need to create Luggage object and append all the data submitted from client, as well as, adding to database and blockchain
    #maybe auto generate Tag ID????????????????? 
    #need to store timestamp 
    #return an array of data, need to send it also 

    return render(request, 'addresult.html')

def testLuggage(request):

    luggageBlock = LuggageBlockchain.objects.all()  #gets all luggage objects in database 

    context = {
        'luggage' : luggageBlock
    }

    return render(request, 'testpage.html', context)

def create(request):
    # validate users
    valid, result = LuggageBlockchain.objects.validateRegister(request.POST)

    # print(result)

    # luggage = LuggageBlockchain.objects.all()

    # pending = {'transactions':[]}
    # transit = {'transactions':[]}
    # arrived = {'transactions':[]}
    
    # testBlock = Blockchain()
    
    # for l in luggage:
    #     # di = {"tagID":l.tag_id, "name":l.name, "transit":l.transit}  
    #     if l.transit == 'T':
    #         transit['transactions'].append({"tagID":l.tag_id, "name":l.name, "transit":l.transit})
    #         a = testBlock.add(transit)
    #     elif l.transit == 'A':
    #         arrived['transactions'].append({"tagID":l.tag_id, "name":l.name, "transit":l.transit})
    #         b = testBlock.add(arrived)
    #     else:
    #         pending['transactions'].append({"tagID":l.tag_id, "name":l.name, "transit":l.transit})
    #         c = testBlock.add(pending)
    
    # t = testBlock.getTransactions('all')

    # print(t)

    # redirect to user dashboard
    return redirect('testLuggage')