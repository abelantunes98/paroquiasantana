from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.

def menu(request):
    return render(request, 'menu.html')