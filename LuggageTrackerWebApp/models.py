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

    #new added variables accoridng to blockchain class 
    Luggage_status_choices = (('Arrived', 'Arrived'), ('In Transit', 'In Transit'))
    status = models.CharField(max_length=20, choices=Luggage_status_choices) #luggage transit status can be either 'Arrived' or 'In Transit'

    Flagged_choices = (('N', 'N'), ('Y', 'Y'))
    flagged = models.CharField(max_length=1, choices=Flagged_choices) #can be either 'N' or 'Y'

    Digital_Signature_choices = (('Approved', 'Approved'), ('Disapproved', 'Disapproved'), ('Waiting', 'Waiting')) 
    digital_signature = models.CharField(max_length=20, choices=Digital_Signature_choices) #can be either 'approved' or 'disapproved' or 'waiting'