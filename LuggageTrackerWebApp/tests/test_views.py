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
        self.contact_url = reverse('contact')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')

    def test_home_page(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200) #testing to see if the client gets correct return response 
        self.assertTemplateUsed(response, 'home.html') #testing to see if the client gets the template home.html 
    
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

    def test_result_page(self):
        response = self.client.get(self.result_url)

        self.assertEquals(response.status_code, 302)

    def test_createluggage_page(self):
        response = self.client.get(self.createluggage_url)

        self.assertEquals(response.status_code, 302)
 
    def test_faq_page(self):
        response = self.client.get(self.faq_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'FAQ.html')  

    def test_movetoadd_page(self):
        response = self.client.get(self.movetoadd_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add.html')   
    
    def test_addfailed_page(self):
        response = self.client.get(self.addfailed_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'failedpush.html')  

    def test_contact_page(self):
        response = self.client.get(self.contact_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')  

    def test_login(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')  

    def test_logout(self):
        response = self.client.get(self.logout_url)

        self.assertEquals(response.status_code, 302)