from django.urls import path
from .views import login
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
  path('login', login, name="login"),
  path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]