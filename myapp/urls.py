from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
    path('about/', views.about, name='about'),
    path('header/', views.header, name='header'),
    path('project/', views.project, name='project'),
    path('skills/', views.skills, name='skills'), 
]