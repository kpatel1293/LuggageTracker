from django.db import models
from django.db.models.fields import TimeField

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
def getCities():
    f = open('./LuggageTrackerWebApp/airport.txt', 'r')
    fArr = f.read()
    f.close()
    return fArr

#for migrating data to MYSQL database      
class luggage(models.Model):
    tag_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    description = models.TextField(blank=True)
    time_stamp = models.DateTimeField('Time Last Scanned')
    origin_airport = models.CharField(max_length=150)
    transit_airport = models.CharField(max_length=150)
    destination_airport = models.CharField(max_length=150)

class LuggageBlockchain(models.Model):
    
    SIGNTURE = (
        ('NA', 'AWAITING SIGNTURE'),
        ('C', 'CHECKED IN'),
        ('IT', 'IN TRANSIT'),
        ('R', 'REACHED DESTINATION'),
        ('M', 'MISSING'),
        ('D', 'DELAYED'),
        ('BC', 'BAGGAGE CLAIM'),
        ('A', 'RETRIVED BY CUSTOMER'),
        ('E', 'CHECK MEMO FOR ERROR')
    )

    FLAG = (('Y', 'YES'), ('N', 'NO'))

    ORIGIN = (('ORD', 'CHICAGO/ORD'), ('EWR', 'NEWARK/EWR')) # HARD CODED EXAMPLE FOR TESTING

    tag_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    hash_id = models.CharField(null=True, max_length=255, default='AWAITING HASH')
    prev_hash_id = models.CharField(null=True, max_length=255, default='AWAITING HASH')
    timestamp = models.DateTimeField('Time Last Scanned')
    origin_airport = models.CharField(max_length=3, choices=ORIGIN, default='')
    destination_airport = models.CharField(max_length=3, choices=ORIGIN, default='')
    name = models.CharField(max_length=255,default='N/A')
    memo = models.CharField(max_length=255, default='N/A')
    digital_signature = models.CharField(max_length=2, choices=SIGNTURE, default='NA')
    flagged = models.CharField(max_length=1, choices=FLAG, default='N')