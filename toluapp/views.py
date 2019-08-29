from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from toluapp.models import studentForm

# Create your views here.

def home(request):
    temp = get_template('home.html').render()
    return HttpResponse(temp)

def index(request):
    temp = get_template('index.html').render()
    return HttpResponse(temp)

def aboutUs(request):
    temp = get_template('about-us.html').render()
    return HttpResponse(temp)

def contact(request):
    temp = get_template('contact-us.html').render()
    return HttpResponse(temp)

def portfolio(request):    
    temp = get_template('portfolio.html').render()
    return HttpResponse(temp)

def services(request):
    temp = get_template('services.html').render()
    return  HttpResponse(temp)

def privacy(request):
    temp = get_template('privacy.html').render()
    return HttpResponse(temp)

def e404(request):
    temp = get_template('404.html').render()
    return HttpResponse(temp)

def createstudentForm(request):
    fullName = request.POST.get('fullName')
    emailAddress = request.POST.get('emailAddress')
    telephone = request.POST.get('telephone')
    message = request.POST.get('message')

    newstudentForm = studentForm(fullName=fullName, emailAddress=emailAddress, telephone=telephone, message=message)
    newstudentForm.save()

    temp = get_template('contact-us.html').render({'message': 'Your contact form has been sucessfully submitted'})
    return HttpResponse(temp)

def readstudentForm(request):
    studentForms = studentForm.objects.all()
    temp = get_template('form-list.html').render({'studentForms': studentForms})
    return HttpResponse(temp)

def deletestudentForm(request):
    student = studentForm.objects.get(id = int(request.GET.get('id')))
    student.delete()

    return redirect(readstudentForm)

def updatestudentForm(request):
    student = studentForm.objects.get(id = int(request.POST.get('id')))

    studentForm.fullName = request.POST.get('fullName')
    studentForm.emailAddress = request.POST.get('emailAddress')
    studentForm.telephone = request.POST.get('telephone')
    studentForm.message = request.POST.get('message')

    student.save()

    return redirect(readstudentForm)

def contact(request):
    if request.GET.get('id'):
        student = studentForm.objects.get(id = request.GET.get('id'))
        temp = get_template('contact-us.html').render({'studentForm': student, 'info': "Update"})
    else: 
        temp = get_template('contact-us.html').render({'info':"Send Message"})

    return HttpResponse(temp)

    
