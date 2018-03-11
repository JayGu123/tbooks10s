from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'myApp/index.html')
import os
from django.contrib import settings
def upfile(request):
    return render(request, 'myApp/upfile.html')
def savefile(request):
    if request.method == 'POST':
        f = request.FILES['file']
        #文件在服务器端的路径
        filePath = os.path.join(settings.MDEIA_ROOT)
    else:
        return HttpReponse("上传失败")