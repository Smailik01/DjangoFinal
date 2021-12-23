from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *
from .models import *


def homepage(request):
    return render(request, 'mainapp/homepage.html')


def events(request):
    posts = Gallery.objects.all()
    return render(request, 'mainapp/events.html', {'posts': posts})


def teachers(request):
    posts = Teacher.objects.all()
    return render(request, 'mainapp/teachers.html', {'posts': posts})


def contact(request):
    if request.method == "POST":
        form = newMessage(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            mt = form.cleaned_data['mtext']
            reg = Message(name=nm, email=em, mtext=mt)
            reg.save()
            return render(request, 'mainapp/message.html')
    else:
        form = newMessage()
    return render(request, 'mainapp/contact.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = studentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            sm = form.cleaned_data['surname']
            um = form.cleaned_data['username']
            em = form.cleaned_data['email']
            ph = form.cleaned_data['phone']
            reg = Student(name=nm, surname=sm, username=um, email=em, phone=ph)
            reg.save()
            return render(request, 'mainapp/homepage.html')
    else:
        form = studentRegistration()
    return render(request, 'mainapp/register.html', {'form': form})

    
def signup(request):
    return render(request, 'mainapp/signup.html')