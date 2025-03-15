from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greeting(request):
    return HttpResponse("Welcome to my bookstore, I Code and Programme in Python and Django")
