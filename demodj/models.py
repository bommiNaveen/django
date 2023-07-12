
from django.db import models

#Create your models here

class student (models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    fathername = models.CharField(max_length=50)

    

    class Meta:
        verbose_name = ("student")
        verbose_name_plural = ("students")

    def __str__(self):
        return self.name

    
