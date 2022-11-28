from django.http import HttpResponse
from django.shortcuts import render
from . models import *

# Create your views here.
def home(request):
    obj = Place.objects.all()
    team = Team.objects.all()
    return render(request, 'index.html',{"obj": obj,"team": team})

