from django.db import models

# Create your models here.

class Tugas (models.Model):
    Task = models.TextField()
    subject = models.CharField(max_length=100)
    info = models.CharField(max_length=150)
    #Status = models.TextField()
    #Action = models.TextField()
