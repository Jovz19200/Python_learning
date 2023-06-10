from django.shortcuts import render
# import http response 
# view module is a request handler module
from django.http import HttpResponse

def say_hello(request):
    x= 1
    y = 2
    # in this function we can pull data from DB
    # send emails
    # transform data and so on
    return render(request, 'hello.html', {'name': 'Jovan'})
# Create your views here.
