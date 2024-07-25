from django.db import models

# Create your models here.
class Student(models.Model):
    name =models.CharField(max_length=255,null=True,blank=True)
    age=models.PositiveIntegerField(null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    phone =models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.name)
