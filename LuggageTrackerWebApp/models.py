from django.db import models
from django.db.models.fields import TimeField
from datetime import datetime

# Create your models here. Create data classes here and objects will be created in "views.py" and passing the object to htmls

#Object Data class

class LuggageManager(models.Manager):
    # validate registeration
    def validateLuggage(self,form_data):
        # store user to database
        addLuggage = self.create(description=form_data['description'],time_stamp=datetime.now(),origin_airport=form_data['origin_airport'],transit_airport=form_data['transit_airport'],destination_airport=form_data['destination_airport'])
        
        return addLuggage.tag_id

#for migrating data to MYSQL database      
class luggage(models.Model):
    tag_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    description = models.TextField(blank=True)
    time_stamp = models.DateTimeField('Time Last Scanned', default=datetime.now())
    origin_airport = models.CharField(max_length=150)
    transit_airport = models.CharField(max_length=150)
    destination_airport = models.CharField(max_length=150)

    #new added variables accoridng to blockchain class 
    STATUS = (('Arrived', 'Arrived'), ('In Transit', 'In Transit'))
    status = models.CharField(max_length=20, choices=STATUS, default='n/a') #luggage transit status can be either 'Arrived' or 'In Transit'

    FLAG = (('N', 'N'), ('Y', 'Y'))
    flagged = models.CharField(max_length=1, choices=FLAG, default='N') #can be either 'N' or 'Y'

    SIGNTURE = (('Approved', 'Approved'), ('Disapproved', 'Disapproved'), ('Waiting', 'Waiting')) 
    digital_signature = models.CharField(max_length=20, choices=SIGNTURE, default='Waiting') #can be either 'approved' or 'disapproved' or 'waiting'

    # call luggage manager
    objects = LuggageManager()

    # print user created
    def __str__(self):
        return str(self.tag_id)
