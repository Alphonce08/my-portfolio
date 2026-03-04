from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def contact(request):
    return render(request, 'contact.html')


def header(request):   
    return render(request, 'header.html')

def experience(request):
    return render(request, 'experience.html')

def about(request):
    return render(request, 'about.html')




def education(request):
    education_data = [
        {
            "icon": "🎓",
            "period": "Jan 2023 - Dec 2025",
            "institution": "eMobilis Technology Training Institute",
            "degree": "Diploma in Information Technology",
            "details": "Distinction"
        },
        {
            "icon": "🏫",
            "period": "2017 - 2021",
            "institution": "Motiret Secondary School",
            "degree": "Kenya Certificate of Secondary Education (KCSE)",
            "details": "Grade: C (plain)"
        },
        {
            "icon": "📘",
            "period": "2007 - 2016",
            "institution": "Chesegem Primary School",
            "degree": "Kenya Certificate of Primary Education (KCPE)",
            "details": "Score: 291 out of 500"
        }
    ]

    context = {
        "education": education_data
    }

    return render(request, "education.html", context)



def experience(request):
    experiences = [
        {
            "period": "Oct 2022 - March 2023",
            "title": "Annotation",
            "company": "Remotask",
            "responsibilities": [
                "Task Execution & Performance",
                "Training and Onboarding Responsibilities",
                "Quality Assurance & Data Review",
                "Legal & Professional Obligations"
            ]
        }
    ]

    context = {
        "experiences": experiences
    }

    return render(request, "experience.html", context)



