from django.test import TestCase, Client
from django.urls import reverse 
from django.contrib.auth.models import User, auth
from django.contrib.auth import SESSION_KEY



class Test_LogInOut_Form(TestCase):

    #create dummy user to test
    @classmethod
    def setUpUser(cls):
        cls.user1 = User.objects.create_user(username = 'test', password = 'password123', email= 'test@example.com')


    def login(self, username='test', password='password123', url='/login/'):
        response = self.client.post(url, {
            'username': username,
            'password': password,
        })
        self.assertIn(SESSION_KEY, self.client.session)
        return response

    def logout(self):
        response = self.client.get('/admin/logout/')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(SESSION_KEY, self.client.session)