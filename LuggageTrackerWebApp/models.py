from django.db import models
from django.db.models.fields import TimeField

# Create your models here. Create data classes here and objects will be created in "views.py" and passing the object to htmls

#Object Data class

#for migrating data to MYSQL database      
class luggage(models.Model):
    tag_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    description = models.TextField(blank=True)
    time_stamp = models.DateTimeField('Time Last Scanned')
    origin_airport = models.CharField(max_length=150)
    transit_airport = models.CharField(max_length=150)
    destination_airport = models.CharField(max_length=150)

class LuggageManager(models.Manager):
    # validate registeration
    def validateRegister(self,form_data):
        # empty errors list
        errors = []

        # check if any errors
        if errors: # if true, display errors
            return (False, errors)

        # # check if user exists
        # try:
        #     check_user = self.get(email=form_data['email'])
        #     errors.append('User already exists')
        #     return (False, errors)
        # # if user does not exist
        # except:

        name = form_data['name']
        # hash_pwd = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())

        # store user to database
        addLuggage = self.create(name=form_data['name'])
        
        return (True, addLuggage.tag_id)

class LuggageBlockchain(models.Model):
    
    # SIGNTURE = (
    #     ('NA', 'AWAITING SIGNTURE'),
    #     ('C', 'CHECKED IN'),
    #     ('IT', 'IN TRANSIT'),
    #     ('R', 'REACHED DESTINATION'),
    #     ('M', 'MISSING'),
    #     ('D', 'DELAYED'),
    #     ('BC', 'BAGGAGE CLAIM'),
    #     ('A', 'RETRIVED BY CUSTOMER'),
    #     ('E', 'CHECK MEMO FOR ERROR')
    # )

    # FLAG = (('Y', 'YES'), ('N', 'NO'))
    TYPEOFTRANSIT = (('P', 'PENDING'), ('T', 'TRANSIT'), ('A', 'ARRIVED'))

    # ORIGIN = (('ORD', 'CHICAGO/ORD'), ('EWR', 'NEWARK/EWR')) # HARD CODED EXAMPLE FOR TESTING

    tag_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # hash_id = models.CharField(null=True, max_length=255, default='AWAITING HASH')
    # prev_hash_id = models.CharField(null=True, max_length=255, default='AWAITING HASH')
    # timestamp = models.DateTimeField('Time Last Scanned')
    # origin_airport = models.CharField(max_length=3, choices=ORIGIN, default='')
    # destination_airport = models.CharField(max_length=3, choices=ORIGIN, default='')
    name = models.CharField(max_length=255,default='N/A')
    transit = models.CharField(max_length=1, choices=TYPEOFTRANSIT, default='P')
    # memo = models.CharField(max_length=255, default='N/A')
    # digital_signature = models.CharField(max_length=2, choices=SIGNTURE, default='NA')
    # flagged = models.CharField(max_length=1, choices=FLAG, default='N')

    # call luggage manager
    objects = LuggageManager()

    # print user created
    def __str__(self):
        return str(self.tag_id)