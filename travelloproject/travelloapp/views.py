from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Destiny, People


def demo(request):
     dest=Destiny.objects.all()
     desti=People.objects.all()
     return render(request,'index.html',{'plac':dest,'place':desti})

