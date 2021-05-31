from django.test import TestCase, Client #using dummy client to test 
from django.urls import reverse
from LuggageTrackerWebApp.models import Luggage, LuggageManager, Blocks, BlockchainManager, Airport

class TestViews(TestCase):

    #creating dummy client including dummy data for testing
    def setUpTestClient(self):
        self.client = Client()