#This file is created manually 

from django.urls import path

from . import views  

urlpatterns = [ 
    path('', views.home, name='home'), #home() function will be define in "views.py", which is called to return Webpage to client
    path('search', views.search, name='search'), #search() function called when user submits Luggage Tag ID, function defined in "views.py"
    path('notfound', views.notfound, name='notfound'), #notfound() directs to html page when luggage Tag ID not found in database
    path('movetoadd', views.movetoadd, name='movetoadd'), #movetoadd() function called when user clicks on add button on homepage, function defined in "views.py"
    path('addLuggage/<int:tag_id>', views.addLuggage, name='addLuggage'), #addLuggage() posting new add luggage result
    path('movetologin', views.movetologin, name='movetologin'), #movetologin() function called when user clicks on login button to take to login in page
    path('login', views.login, name='login'), #login() function called with user signin take back to home page 
    path('result/<int:tag_id>', views.result, name='result'),
    path('createLuggage', views.createLuggage, name='createLuggage'),
    path('FAQ', views.faq, name='FAQ'), #FAQ() function called with user signin take back to home page
    path('movetoadd', views.autocomplete, name='autocomplete'),
# MASTER ------------
#     path('result/<int:tag_id>', views.result, name='result'), #result() posting search results 
#     path('createLuggage', views.createLuggage, name='createLuggage'), #createLuggage() push new luggage data 
#     path('addfailed', views.addfailed, name='addfailed') #addfailed() directs to html page new added luggage failed
]
