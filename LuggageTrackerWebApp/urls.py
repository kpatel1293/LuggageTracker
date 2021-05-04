#This file is created manually 

from django.urls import path

from . import views  

urlpatterns = [ 
    path('', views.home, name='home'), #home page , the home() function will be define in "views.py", which is called to return something to client
    path('add', views.add, name='add') #add fucntion called when user submits, the fucntion is defined in "views.py"
]