from django.test import TestCase, Client
from django.urls import reverse 
from django.contrib.auth.models import User, auth



#class Test_LogInOut_Form(TestCase):

    #create dummy user to test
    #def setUpUser(self):
        #self.client = Client()
        #self.user = User.objects.create_user(username='admin', password = '123456789', email='test@example.com')
        #self.user.save()
    
    #def test_login_form(self):
        #client = self.client 
        #user_login = client.login(username = 'admin', password = '123456789')
        
        #self.assertTrue(user_login)