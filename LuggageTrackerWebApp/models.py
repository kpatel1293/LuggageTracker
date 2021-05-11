from django.db import models

# Create your models here. Create data classes here and objects will be created in "views.py" and passing the object to htmls

#Object Data class 
class luggage(models.Model):
    tag_id = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    time_stamp = models.DateTimeField('Time Last Scanned')
    origin_airport = models.CharField(max_length=120)
    transit_airport = models.CharField(max_length=120)
    destination_airport = models.CharField(max_length=120)

#Example
#this code will be included in "views.py"

#form .models import obj 

#def index(request):
#    object1 = obj() 
#    object1.name = 'Jack'

#    dests = [object1, object2]  #this will allow you to pass multiple datas in array form, just change bleow {'dests' : dests}

#    return render(request, "home.html", {'object1' : object1})


#in the html file you will need to include a for loop to retrieve the dynamic array of objects to display on webpage
# {% for dest in dests %}
#
# you html code 
#
# {% endfor %}


    
