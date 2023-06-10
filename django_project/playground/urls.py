#url config module for our app
# which we have to import to our main url config 
# we have to make url patterns to connect path to the reference
# urlpatterns must be wrote in small letters and must be an array
from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.say_hello)
]