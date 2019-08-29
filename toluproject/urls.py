"""toluproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView
from toluapp.views import aboutUs, createstudentForm, updatestudentForm, readstudentForm, deletestudentForm, index, contact, privacy, e404, services, portfolio, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/', aboutUs),
    path('contact-us/', contact),
    path('privacy/', privacy),
    path('404/', e404),
    path('services/', services),
    path('portfolio/', portfolio),
    path('index.html/', index),
    path('create-studentForm/', createstudentForm),
    path('read-studentForm/', readstudentForm),
    path('delete-studentForm/', deletestudentForm),
    path('update-studentForm/',updatestudentForm),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'))
   
]
