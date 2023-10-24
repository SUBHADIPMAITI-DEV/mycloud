from django.db import models

# Create your models here.

class index(models.Model):
    username = models.CharField(max_length=120, null=False)
    password = models.CharField(max_length=30, null=False)



# class upload(models.Model):
#     fileupload = models.ImageField(upload_to='images/')

# models.py

class FileModel(models.Model):
    file = models.FileField(upload_to='uploads/')
