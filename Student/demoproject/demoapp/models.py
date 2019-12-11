from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    rollno=models.IntegerField()
    school=models.CharField(max_length=60)
    def __str__(self):
        return self.name
