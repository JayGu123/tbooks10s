from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Students,Grades
# Create your views here.
def index(request):
    #return HttpResponse('hello')
    stu = Students.objects.get(pk = 1)
    return render(request, 'mobban/index.html', {'student':stu, 'num':10, 'testlist':['good','well','great','amazing','awesome']})

def students(request):
    studentslist = Students.objects.all()
    return render(request, 'mobban/students.html', {'list': studentslist})