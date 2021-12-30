from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Instructor(models.Model):
    name                = models.CharField(max_length = 20)
    salary              = models.IntegerField()
    teaches             = models.CharField(max_length= 20)

    def __str__(self):
        return self.name   

class Student(models.Model):
    std_name                = models.CharField(max_length=20)
    roll                    = models.CharField(max_length=4)
    takes_course            = models.CharField(max_length=20)
    instructor              = models.ForeignKey(Instructor,on_delete=CASCADE)

    def __str__(self):
        return self.std_name      

   
