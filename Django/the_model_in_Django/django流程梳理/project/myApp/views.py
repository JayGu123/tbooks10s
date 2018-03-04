from django.shortcuts import render
from django.http import HttpResponse
from .models import Grades,Students
# Create your views here.
def welcome(request):
    return render(request,'myApp/welcome.html')

def students(request):
    studentsList=Students.stuObj2.all()
    return render(request,'myApp/students.html',{'students':studentsList})
#限制查询集，使用下标的方式
def students2(request):
    studentsList=Students.stuObj2.all()[0:1]
    return render(request,'myApp/students.html',{'students':studentsList})
#分页显示学生
def stupage(request,page):
    #0-5  5-10  10-15
    #1    #2    #3
    #page*5
    page=int(page)
    studentsList=Students.stuObj2.all()[(page-1)*5:page*5]
    return render(request,'myApp/students.html',{'students':studentsList})
from django.db.models import Max
def studentsearch(request):
    #studentsList=Students.stuObj2.filter(sname__startswith="林")
    #studentsList=Students.stuObj2.filter(sname__contains="周")
    studentsList=Students.stuObj2.filter(pk__in=[1])
    maxPk=Students.stuObj2.aggregate(Max('id'))
    print(maxPk)
    #studentsList=Students.stuObj2.filter(lastTime__year=2017)
    #studentsList = Students.stuObj2.filter(students__scontend__contains="周杰伦")
    return render(request,'myApp/students.html',{'students':studentsList})


from django.db.models import F,Q
def grades(request):
    g=Grades.objects.filter(ggitlnum__gt=F('gboynum'))
    print(g)
#def addstudents(request):
    #grade=Grades.objects.get(pk=1)
    #stu=Students.createStudent("周杰伦",grade,"哎哟，不错哦",True,"2018-3-4","2018-3-4")
    #stu.save()
    #return(HttpResponse("学生创建成功"))
#def addstudents2(request):
    #grade=Grades.objects.get(pk=1)
    #stu=Students.stuObj2.createStudent("林俊杰",grade,"我喜欢周杰伦",True,"2018-3-4","2018-3-4")
    #stu.save()
    #return HttpResponse('****')
