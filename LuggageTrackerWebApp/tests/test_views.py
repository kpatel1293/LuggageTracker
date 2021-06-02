from django.test import TestCase, Client
from django.urls import reverse 
from LuggageTrackerWebApp.models import Luggage, LuggageManager, Blocks, BlockchainManager, Airport


class TestViews(TestCase):
    
    #setup dummy client to test the views and templates
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.search_url = reverse('search')
        self.notfound_url = reverse('notfound')
        self.movetologin_url = reverse('movetologin')
        self.result_url = reverse('result', args=[1])
        self.createluggage_url = reverse('createLuggage')
        self.faq_url = reverse('FAQ')
        self.movetoadd_url = reverse('autocomplete')
        self.addfailed_url = reverse('addfailed')

    def test_home_page(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html') #testing to see if the client gets the template home.html 
    
    #needs more testing for redirects 
    def test_search_page(self):
        response = self.client.get(self.search_url)

        self.assertEquals(response.status_code, 302) #302 response is for redirects 

    def test_notfound_page(self):
        response = self.client.get(self.notfound_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'notfound.html')  
    
    def test_movetologin_page(self):
        response = self.client.get(self.movetologin_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')   

    #needs more testing for redirects 
    def test_result_page(self):
        response = self.client.get(self.result_url)

        self.assertEquals(response.status_code, 302)

    #needs more testing for redirects 
    def test_createluggage_page(self):
        response = self.client.get(self.createluggage_url)

        self.assertEquals(response.status_code, 302)

    #needs to add FAQ.html to pass 
    #def test_faq_page(self):
        #response = self.client.get(self.faq_url)

        #self.assertEquals(response.status_code, 200)
        #self.assertTemplateUsed(response, 'FAQ.html')  

    def test_movetoadd_page(self):
        response = self.client.get(self.movetoadd_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add.html')   
    
    def test_addfailed_page(self):
        response = self.client.get(self.addfailed_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'failedpush.html')  