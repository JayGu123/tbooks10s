from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Students,Grades
# Create your views here.
def index(request):
    #return HttpResponse('hello')
    stu = Students.objects.get(pk = 1)
    return render(request, 'mobban/index.html', {'student':stu, 'num':10, 'testlist':['good','well','great','amazing','awesome'], 'code':'<h1>jay is a handsomeman</h1>'})

def students(request):
    studentslist = Students.objects.all()
    return render(request, 'mobban/students.html', {'list': studentslist})

def good(request, pages):
    return render(request, 'mobban/good.html', {'page':pages})

def main(request):
    return render(request, 'mobban/main.html')

def postfile(request):
    return render(request, 'mobban/postfile.html')
def showinfo(request):
    name = request.POT.get('username')
    pwd = request.POST.get('password')
    return render(request, 'mobban/showinfo.html', {'username':name ,'password':pwd})