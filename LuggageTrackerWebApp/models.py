from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TimeField
# from datetime import datetime
# import time
from django.utils import timezone


# Create your models here. Create data classes here and objects will be created in "views.py" and passing the object to htmls

#Object Data class

class LuggageManager(models.Manager):
    # validate registeration
    def validateLuggage(self,form_data):
        # store user input new luggge to database 
        addLuggage = self.create(
            description=form_data['description'],
            origin_airport=form_data['origin_airport'],
            transit_airport=form_data['transit_airport'],
            destination_airport=form_data['destination_airport']
        )
        
        return addLuggage.tag_id

#for migrating data to MYSQL database      
class Luggage(models.Model):
    tag_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    description = models.TextField(blank=True)
    time_stamp = models.TimeField('Time Last Scanned', default=timezone.now)
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

class BlockchainManager(models.Manager):
    # validate registeration
    def validateBlockchain(self,blockchain, luggage):
        # store user input new luggge to database 
        addBlock = self.create(
            index=blockchain['index'],
            transactions=luggage,
            timestamp=blockchain['timestamp'],
            prevHash=blockchain['prevHash'],
            nonce=blockchain['nonce'],
            hash_curr=blockchain['hash']
        )

        return addBlock.hash_curr

    def updateBlockchain(self,id,blockchain):
        updateBlock = self.filter(hash_curr=id).update(index=blockchain['index'],timestamp=blockchain['timestamp'],prevHash=blockchain['prevHash'],nonce=blockchain['nonce'],hash_curr=blockchain['hash'])
        return blockchain['hash']

class Blocks(models.Model):
    index = models.IntegerField(primary_key=True)
    transactions = models.OneToOneField(Luggage, on_delete=CASCADE)
    timestamp = models.FloatField()
    prevHash = models.CharField(max_length=150)
    nonce = models.IntegerField(default=0)
    hash_curr = models.CharField(max_length=150)

    # call luggage manager
    objects = BlockchainManager()

    # print user created
    def __str__(self):
        return str(self.hash_curr)

class Airport(models.Model):
    name = models.TextField(blank=True)
    municipality = models.CharField(max_length=150)
    iatacode = models.CharField('IATA Code', max_length=10)
    objects = models.Manager()

    def __str__(self):
       return str(self.name)
