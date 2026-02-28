from django.db import models

# Create your models here.

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()  # e.g., 1-10 scale

    def __str__(self):
        return self.name

class Hobby(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name