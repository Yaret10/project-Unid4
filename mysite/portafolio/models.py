from django.db import models

# Create your models here.

class Projects(models.Model):
    Photo = models.ImageField(upload_to='images/', null=True, blank=True)
    Title =  models.CharField(max_length=100)
    Description =  models.TextField()
    Tags =  models.CharField(max_length=100)
    url_gitHub = models.CharField(max_length=100)


    
