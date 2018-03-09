from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'myApp/home.html')

def attributes(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse('jay chou!')


#获取get传递的数据
def get1(request):
    a = request.GET['a']
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a+" "+b+" "+c)

def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c = request.GET.get('c')
    return HttpResponse(a1+" "+a2+" "+c)
#POST
def showregister(request):
    return render(request,'myApp/register.html')
def register(request):
    name = request.POST.get("name")
    gender = request.POST.get("gender")
    age = request.POST.get("age")
    hobby = request.POST.getlist("hobby")
    print(name)
    print(gender)
    print(age)
    print(hobby)
    return HttpResponse('hahaha')

#reponse
def showresponse(request):
    res = HttpResponse()
    print(res.content)
    print(res.charset)
    print(res.status_code)
    print(res.content-type)
    return res
#cookies
def cookietest(request):
    res = HttpResponse()
    cookie = res.COOKIES
    res.write("<h1>"+cookie['jay']+"<h1/>")
    #cookie = res.set_cookie("jay","singer")
    return res


#重定向
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import redirect
def redirect1(request):
    #return HttpResponseRedirect("jay/redirect2")
    return redirect('/redirect2/')
def redirect2(request):
    return HttpResponse('重定向后的视图')



#session
def index(request):
    #取session
    username = request.session.get('name','游客')
    return render(request, 'myApp/index.html',{'username':username})
def login(request):
    return render(request, 'myApp/login.html')
def showindex(request):
    print('*****')
    username = request.POST.get('username')
    print(username)
    #存储session
    request.session['name'] = username
    request.session.set_expire(0)
    return redirect('/index/')
from django.contrib.auth import logout
def quit(request):
    #清除session
    logout(request)
    #request.session.clear()
    #request.session.flush()
    return redirect('/index/')