from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User 
from faker import Faker

class LoginAPI(APITestCase):
  def setUp(self) :
      self.fake =Faker()  
      self.loginUrl = reverse("login")
      self.email_and_password = self.fake.email()
      self.user = User.objects.create(
      email=self.email_and_password,
      username=self.email_and_password,
      first_name=self.fake.name(),
      last_name=self.fake.name(),
      )
      self.user.set_password(self.email_and_password)
      self.user.save()
      return super().setUp()
  def tearDown(self) :
      return super().tearDown()



class TestView(LoginAPI):

  def test_empty_data(self):
    data = {}
    response =  self.client.post(self.loginUrl,data)
    self.assertEqual(response.status_code , 400) 
  
  def test_empty_data_email(self):
    data = {
      "email":"",
      "password":self.email_and_password
    }
    response =  self.client.post(self.loginUrl,data)
    self.assertEqual(response.status_code , 400) 
  
  def test_empty_data_password(self):
    data = {
      "email":self.email_and_password,
      "password":""
    }
    response =  self.client.post(self.loginUrl,data)
    self.assertEqual(response.status_code , 400) 
  
  
  def test_not_valid_email(self):
    data = {
      "email":"dsfcdsdsd",
      "password":"12234353454"
    }
    response =  self.client.post(self.loginUrl,data)
    self.assertEqual(response.status_code , 400) 
  
  
  def test_not_valid_cardintional(self):
    data = {
      "email":"dsfcdsdsd@dsds.com",
      "password":"12234353454"
    }
    response =  self.client.post(self.loginUrl,data)
    self.assertEqual(response.status_code , 401) 
  
  
  def test_valid_cardintional(self):
    data = {
      "email":self.email_and_password,
      "password":self.email_and_password
    }
    response =  self.client.post(self.loginUrl,data)
    self.assertEqual(response.status_code , 200) 

  

  


