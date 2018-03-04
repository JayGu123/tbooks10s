from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Grades,Students
def index(request):
    return HttpResponse('jay is a good man')

def detail(request,num):
    info='cannot find the page'
    #return HttpResponse("detail-%s" % info)
    return HttpResponse("detail-%s" % num)

def grades(request):
    #去模板里取数据
    gradesList=Grades.objects.all()
    #将数据传递给模板,模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request,'myApp/grades.html',{"grades":gradesList})

def students(request):
    studentsList=Students.objects.all()
    return render(request,'myApp/students.html',{'students':studentsList})

def gradesStudents(request,num):
    #获得对应的版班级对象
    grade=Grades.objects.get(pk=num)
    #获得对应班级下的学生对象（所有）
    studentsList=grade.students_set.all()
    return render(request,'myApp/students.html',{"students":studentsList})