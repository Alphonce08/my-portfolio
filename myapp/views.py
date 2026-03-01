from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def contact(request):
    return render(request, 'contact.html')


def education(request):
    return render(request, 'education.html')


def experience(request):
    return render(request, 'experience.html')

