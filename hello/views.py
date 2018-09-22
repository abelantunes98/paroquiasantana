from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.

def index(request):
    return render(request, 'index.html')

def news(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'news.html', {'greetings': greetings})