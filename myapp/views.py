# portfolio_app/views.py
from django.shortcuts import render
from .models import Experience, Skill, Hobby

def index(request):
    return render(request, 'index.html')

def experience(request):
    experiences = Experience.objects.all()
    return render(request, 'experience.html', {'experiences': experiences})

def skills(request):
    skills = Skill.objects.all()
    hobbies = Hobby.objects.all()
    return render(request, 'skills.html', {'skills': skills, 'hobbies': hobbies})