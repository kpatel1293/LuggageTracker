from django.test import TestCase
from LuggageTrackerWebApp.models import luggage
import datetime
from django.test.utils import freeze_time #for testing datetime to stop the datetime for the test


# Create your tests here.


#Testing models 
#class TestModels(TestCase):

    #Creating object Luggage with dummy data to test 
    #@freeze_time("2021-05-26") #CHANGE THIS depending on current date for testing datetime
    #@classmethod
    #def setUpTestData(cls):
        #luggage.objects.create(
        #description = 'Samsonite Red ASTELL',
        #time_stamp = datetime.datetime.now(),
        #origin_airport = 'Chicago O Hare International Airport (ORD)',
        #transit_airport = 'Los Angeles International Airport (LAX)',
        #destination_airport = 'Seattle-Tacoma International Airport (SEA)',
        #status = 'In Transit',
        #flagged = 'N',
        #digital_signature = 'Waiting'
    #)
    
    #def test_luggage_tagID(self):
        #testObject = luggage.objects.get(tag_id = 1)
        #tagID_label = testObject._meta.get_field('tag_id').verbose_name
        #self.assertEqual(tagID_label, 1)

    #def test_luggage_description(self):
        #testObject = luggage.objects.get(tag_id = 1)
        #description_label = testObject._meta.get_field('description').verbose_name
        #self.assertEqual(description_label, 'Samsonite Red ASTELL')
