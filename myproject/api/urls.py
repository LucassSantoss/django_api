from django.urls import path
from .views import HelloWorld, CreateUser

urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello_world'),
    path('register/', CreateUser.as_view(), name='register'),
]
