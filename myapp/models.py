from django.db import models

# Create your models here.

class HomeData(models.Model):
    fullname = models.CharField(max_length=100)
    keywords = models.CharField(max_length=100)
    instaurl = models.CharField(max_length=300)
    fburl = models.CharField(max_length=300)
    linkedinurl = models.CharField(max_length=300)
    githuburl = models.CharField(max_length=300)
    xurl = models.CharField(max_length=300)
    description = models.CharField(max_length=1000,default="")

class Skills(models.Model):
    image = models.ImageField(upload_to="skills/",null=False,blank=False)

class Projects(models.Model):
    title = models.CharField(max_length=100)
    technologies = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="projects/",null=False,blank=False)
    sourcecode = models.CharField(max_length=1000)

class Education(models.Model):
    startYear = models.IntegerField()
    endYear = models.IntegerField()
    instituteName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    stream = models.CharField(max_length=100)

class Experience(models.Model):
    startYear = models.IntegerField()
    endYear = models.IntegerField()
    designation = models.CharField(max_length=50)
    companyName = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobilenumber = models.CharField(max_length=10)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500)