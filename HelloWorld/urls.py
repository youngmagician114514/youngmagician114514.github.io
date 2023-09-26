"""
URL configuration for HelloWorld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# urlpatterns = [
#     path("admin/", admin.site.urls),
# ]

# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('index.html', views.index_view, name='index'),
    path('item01.html', views.item01_view, name='item01'),
    path('item02.html', views.item02_view, name='item02'),
    path('item03.html', views.item03_view, name='item03'),
    path('item04.html', views.item04_view, name='item04'),
    path('about.html', views.about_view, name='about'),
    path('form.html', views.form_view, name='form'),
    path('form-comp.html', views.formcomp_view, name='form_comp'),
    path('contact/', views.contact_form, name='contact_form'),

    # path('', views.index_view, name='index'),
    # path('item01.html', views.op_view('item01.html'), name='item01'),
    # path('item02.html', views.op_view('item02.html'), name='item02'),
    # path('item03.html', views.op_view('item03.html'), name='item03'),
    # path('item04.html', views.op_view('item04.html'), name='item04'),
    # path('about.html', views.op_view('about.html'), name='about'),
    # path('form.html', views.op_view('form.html'), name='form'),
    # path('form-comp.html', views.op_view('form-comp.html'), name='form_comp'),

]
