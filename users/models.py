from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken

class User(AbstractUser):
  email = models.EmailField(unique=True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
  
  def tokens(self):
    token = RefreshToken.for_user(self)
    return {
        'refresh': str(token),
        'access': str(token.access_token)
    }
  def __str__(self):
    return self.username