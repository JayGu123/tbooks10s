from django.shortcuts import render
from django.http import HttpResponse
from .models import Grades,Students
# Create your views here.
def welcome(request):
    return render(request,'myApp/welcome.html')


