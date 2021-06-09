from django.db.models.base import Model
from django.test import TestCase
from LuggageTrackerWebApp.models import Luggage, LuggageManager, Blocks, BlockchainManager, Airport
from django.utils import timezone
from django.test.utils import freeze_time #for testing datetime to stop the datetime for the test


# Create your tests here.
#Testing models 

class Test_Luggage(TestCase):

    #Creating object Luggage with dummy data to test 
    #@freeze_time("2021-05-26") #CHANGE THIS depending on current date for testing datetime
    @classmethod
    def setUpTestData(cls):
        Luggage.objects.create(
            #tag_id is auto created
            description = 'Samsonite Red ASTELL',
            time_stamp = timezone.now(),
            origin_airport = 'Chicago O Hare International Airport (ORD)',
            destination_airport = 'Seattle-Tacoma International Airport (SEA)',
            #status = 'Checked In',         #using default instead 
            #flagged = 'N',         #using default instead 
            #digital_signature = 'Awaiting Signture'    #using default instead 
        )

    #testing/checking labels if correct when created
    def test_luggage_description(self):
        testObject = Luggage.objects.get(tag_id=1)
        description_label = testObject._meta.get_field('description').verbose_name
        self.assertEquals(description_label, 'description')

    def test_luggage_timestamp(self):
        testObject = Luggage.objects.get(tag_id=1)
        timestamp_label = testObject._meta.get_field('time_stamp').verbose_name
        self.assertEquals(timestamp_label, 'Time Last Scanned')
    
    def test_luggage_origin_airport(self):
        testObject = Luggage.objects.get(tag_id=1)
        OriginAirport_label = testObject._meta.get_field('origin_airport').verbose_name
        self.assertEquals(OriginAirport_label, 'origin airport')
    
    def test_luggage_destination_airport(self):
        testObject = Luggage.objects.get(tag_id=1)
        DestinationAirport_label = testObject._meta.get_field('destination_airport').verbose_name
        self.assertEquals(DestinationAirport_label, 'destination airport')

    def test_luggage_status(self):
        testObject = Luggage.objects.get(tag_id=1)
        status_label = testObject._meta.get_field('status').verbose_name
        self.assertEquals(status_label, 'status')
    
    def test_luggage_flagged(self):
        testObject = Luggage.objects.get(tag_id=1)
        flagged_label = testObject._meta.get_field('flagged').verbose_name
        self.assertEquals(flagged_label, 'flagged')

    def test_luggage_digtial_signature(self):
        testObject = Luggage.objects.get(tag_id=1)
        DigitalSig_label = testObject._meta.get_field('digital_signature').verbose_name
        self.assertEquals(DigitalSig_label, 'digital signature')

#Problems with testing blocks 
class TestBlocks(TestCase):

    @classmethod
    def setUpTestData(cls):
        Luggage.objects.create(
            #tag_id is auto created
            description = 'American Tourister',
            time_stamp = timezone.now(),
            origin_airport = 'Chicago O Hare International Airport (ORD)',
            destination_airport = 'Los Angeles International Airport (LAX)',
            #status = 'Checked In',         #using default instead 
            #flagged = 'N',         #using default instead 
            #digital_signature = 'Awaiting Signture'    #using default instead 
        )

        Blocks.objects.create(
            index = 1,
            transactions = Luggage.objects.get(pk= 1),
            timestamp = 234235312,
            prevHash = '12ewkfngwejgwekg9239',
            nonce = 50,
            hash_curr = '932ufnjwe93908u138u501'
        )

    #def test_blocks_index(self):
        #testObject = Blocks.objects.get(pk = 1)
        #index_label = testObject._meta.get_field('index').verbose_name
        #self.assertEquals(index_label, 'index')


class Test_Airport(TestCase):

    @classmethod
    def setUpTestData(cls):
        Airport.objects.create(
            name = 'Chicago O Hare International Airport',
            municipality = 'general',
            airport_name = 'Chicago O Hare International',
            iatacode = 'ORD'
        )
    
    def test_name(self):
        testObject = Airport.objects.get(pk=1)
        name_label = testObject._meta.get_field('name').verbose_name
        self.assertEquals(name_label, 'name')

    def test_municipality(self):
        testObject = Airport.objects.get(pk=1)
        municipality_label = testObject._meta.get_field('municipality').verbose_name
        self.assertEquals(municipality_label, 'municipality')
    
    def test_iatacode(self):
        testObject = Airport.objects.get()
        iatacode_label = testObject._meta.get_field('iatacode').verbose_name
        self.assertEquals(iatacode_label, 'IATA Code')
    
    def test_airport(self):
        testObject = Airport.objects.get(pk=1)
        airport_label = testObject._meta.get_field('airport_name').verbose_name
        self.assertEquals(airport_label, 'airport name')
    