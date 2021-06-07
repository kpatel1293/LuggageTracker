from django.test import SimpleTestCase #testing path URLS without using the database 
from django.urls import reverse, resolve

#importing the functions from views.py to test the path URLS 
from LuggageTrackerWebApp.views import autocomplete, home, search, result, notfound, createLuggage, movetologin, login, faq, addfailed, contact, logout

#class to test path URLS to calling the right functions in views.py
class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('home')
        print(resolve(url)) #just to show which function the path url should be calling to
        self.assertEquals(resolve(url).func, home) #test the path 'home' calls to home function

    def test_search_url(self):
        url = reverse('search')
        print(resolve(url)) 
        self.assertEquals(resolve(url).func, search) 

    def test_notfound_url(self):
        url = reverse('notfound')
        print(resolve(url)) 
        self.assertEquals(resolve(url).func, notfound) 
    
    def test_movetologin_url(self):
        url = reverse('movetologin')
        print(resolve(url)) 
        self.assertEquals(resolve(url).func, movetologin) 

    def test_login_url(self):
        url = reverse('login')
        print(resolve(url)) 
        self.assertEquals(resolve(url).func, login) 
    
    def test_result_url(self):
        url = reverse('result', args=[1]) #just put some tagID arugment to pass 
        print(resolve(url)) 
        self.assertEquals(resolve(url).func, result) 

    def test_createLuggage_url(self):
        url = reverse('createLuggage')
        print(resolve(url)) 
        self.assertEquals(resolve(url).func, createLuggage) 

    def test_FAQ_url(self):
        url = reverse('FAQ')
        print(resolve(url)) 
        self.assertEquals(resolve(url).func, faq) 

    def test_autocomplete_url(self):
        url = reverse('autocomplete')
        print(resolve(url)) 
        self.assertEquals(resolve(url).func, autocomplete) 
    
    def test_addfailed_url(self):
        url = reverse('addfailed')
        print(resolve(url)) 
        self.assertEquals(resolve(url).func, addfailed) 

    def test_contact_url(self):
        url = reverse('contact')
        print(resolve(url)) 
        self.assertEquals(resolve(url).func, contact)

    def test_logout_url(self):
        url = reverse('logout')
        print(resolve(url)) 
        self.assertEquals(resolve(url).func, logout)

