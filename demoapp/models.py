from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    rollnum=models.IntegerField()
    email=models.EmailField()
    phone=models.IntegerField()
