from django.db import models

# Create your models here. Create data classes here and objects will be created in "views.py" and passing the object to htmls

#Object Data class 

#class luggage:
    #TagID : str
    #Description : str
    #TimeStamp : str
    #Origin_Airport : str
    #InTransit_Status : str
    #Current_Location : str 
    #Destination_Airpot : str
      
#for migrating data to MYSQL database      
class luggage(models.Model):
    tag_id = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    time_stamp = models.DateTimeField('Time Last Scanned')
    origin_airport = models.CharField(max_length=150)
    transit_airport = models.CharField(max_length=150)
    destination_airport = models.CharField(max_length=150)