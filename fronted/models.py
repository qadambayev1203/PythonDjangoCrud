from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    sname=models.CharField(max_length=50)
    Email=models.EmailField()
    phone=models.CharField(max_length=15)

    def __str__(self):
        return self.sname+' '+self.name
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])