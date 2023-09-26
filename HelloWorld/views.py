# views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import  HttpResponseRedirect
from django.urls import reverse


def index_view(request):
    return render(request, 'index.html')

def item01_view(request):
    return render(request,'item01.html')

def item02_view(request):
    return render(request,'item02.html')

def item03_view(request):
    return render(request,'item03.html')

def item04_view(request):
    return render(request,'item04.html')

def about_view(request):
    return render(request,'about.html')

def form_view(request):
    return render(request,'form.html')

def formcomp_view(request):
    return render(request,'form-comp.html')

# def op_view(request,name):
#     return render(request,name)
    

def contact_form(request):
    if request.method == 'POST':
            # 处理表单提交数据的逻辑
            # 可以从request.POST中获取表单数据并进行处理
            email = request.POST.get('email')
            comment = request.POST.get('comment')
            
            # 进行进一步的处理，如发送电子邮件或保存到数据库
            
            # 重定向到form-comp.html页面
            return HttpResponseRedirect(reverse('form_comp'))
    else:
            return render(request, 'form.html')