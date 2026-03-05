from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300)
    github_link = models.URLField(blank=True)

    
    


class Experience(models.Model):
    period = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    

class Education(models.Model):
    period = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.institution


