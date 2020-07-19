from django.db import models

# Create your models here.

class jrsUser(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField()
    location = models.CharField(max_length=40)
    company = models.CharField(max_length=30, default='')
    users = models.Manager()

class job(models.Model):
    id = models.IntegerField(primary_key=True)
    postedby = models.CharField(max_length=20, default='Sharon')
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=20)
    jobType = models.CharField(max_length=15)
    salary = models.CharField(max_length=15)
    jobDescription = models.CharField(max_length=800)
    logo = models.ImageField(upload_to = 'static/mainapp/assets/images')
    rank = models.FloatField()
    location = models.CharField(max_length=40, default='Not specified')
    mustmeet1 = models.CharField(max_length=30, default='')
    mustmeet2 = models.CharField(max_length=30, default='')
    mustmeet3 = models.CharField(max_length=30, default='')
    mustmeet4 = models.CharField(max_length=30, default='')
    mustmeet5 = models.CharField(max_length=30, default='')
    mustmeet6 = models.CharField(max_length=30, default='')
    objects = models.Manager()

class companies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=40)
    rank = models.FloatField()
    logo = models.ImageField()
    objects = models.Manager()