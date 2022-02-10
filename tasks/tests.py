from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User 
from .models import Task
from faker import Faker
from django.utils.timezone import now
from datetime import timedelta
# test after authenication jwt token
class TestSetUpAuthenticated(APITestCase):
  def setUp(self) :
      self.fake =Faker()  
      self.tasks_list = reverse("testList")
      self.finished_tasks = reverse("finishedTasks")
      self.unfinished_tasks = reverse("unfinishedTasks")
      self.user = User.objects.create(
      email=self.fake.email(),
      username=self.fake.email(),
      first_name=self.fake.name(),
      last_name=self.fake.name(),
      )
      self.user.set_password(self.fake.email())
      self.user.save()
      self.client.force_authenticate(user=self.user)
      return super().setUp()
  def tearDown(self) :
      return super().tearDown()



class TestView(TestSetUpAuthenticated):

  def test_get_all_user_tasks(self):
    response =  self.client.get(self.finished_tasks)
    self.assertEqual(response.status_code , 200) 
  
  
  def test_get_finished_user_tasks(self):
    response =  self.client.get(self.finished_tasks)
    self.assertEqual(response.status_code , 200) 
  
  
  def test_get_unfinished_user_tasks(self):
    response =  self.client.get(self.unfinished_tasks)
    self.assertEqual(response.status_code , 200) 
  
  
  def test_mark_as_complete_check_expire_date(self):
    task = Task.objects.create(
      user=self.user,
      start_date=now(),
      due_date=now(),
      type_of_task="pending",
      description="sasdsdsdd",
    )
    url = reverse('markAsCompleteTask', kwargs={'task_id':task.id})
    response =  self.client.get(url)

    self.assertEqual(response.status_code , 200) 
    self.assertEqual(response.data['task']["is_complete"],False)
    self.assertEqual(response.data['task']["type_of_task"],"overdue")
  
  
  def test_mark_as_complete_if_the_tesk_is_already_completed(self):
    task = Task.objects.create(
      user=self.user,
      start_date=now(),
      due_date=now()+timedelta(1)  ,
      type_of_task="pending",
      description="sasdsdsdd",
      is_complete=True
    )
    url = reverse('markAsCompleteTask', kwargs={'task_id':task.id})
    response =  self.client.get(url)

    self.assertEqual(task.is_complete,True)
    self.assertEqual(response.status_code , 400) 
  
  
  
  def test_mark_as_complete(self):
    task = Task.objects.create(
      user=self.user,
      start_date=now(),
      due_date=now()+timedelta(1)  ,
      type_of_task="pending",
      description="sasdsdsdd",
    )
    url = reverse('markAsCompleteTask', kwargs={'task_id':task.id})
    response =  self.client.get(url)

    self.assertEqual(response.status_code , 200) 
    self.assertEqual(response.data['task']["is_complete"],True)
    self.assertEqual(response.data['task']["type_of_task"],"finished")

  


##check  jwt tokens  for authentications

class TestSetUpUnAuthenticated(APITestCase):
  def setUp(self) :
      self.fake =Faker()  
      self.tasks_list = reverse("testList")
      self.finished_tasks = reverse("finishedTasks")
      self.unfinished_tasks = reverse("unfinishedTasks")
      self.user = User.objects.create(
      email=self.fake.email(),
      username=self.fake.email(),
      first_name=self.fake.name(),
      last_name=self.fake.name(),
      )
      self.user.set_password(self.fake.email())
      self.user.save()
      return super().setUp()
  def tearDown(self) :
      return super().tearDown()

class TestSetUnautheticates(TestSetUpUnAuthenticated):
  
  def test_unauthenticated_get_all_user_tasks(self):
    response =  self.client.get(self.finished_tasks)
    self.assertEqual(response.status_code , 401) 
  
  
  def test_unauthenticated_get_finished_user_tasks(self):
    response =  self.client.get(self.finished_tasks)
    self.assertEqual(response.status_code , 401) 
  
  
  def test_unauthenticated_get_unfinished_user_tasks(self):
    response =  self.client.get(self.unfinished_tasks)
    self.assertEqual(response.status_code , 401) 

  def test_mark_as_complete(self):
    url = reverse('markAsCompleteTask', kwargs={'task_id':1})
    response =  self.client.get(url)
    self.assertEqual(response.status_code , 401) 


