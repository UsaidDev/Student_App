from django.db import models

# Create your models here.

class Students(models.Model):
    Roll=models.IntegerField(null=True)
    Name=models.CharField(max_length=250)
    Class=models.IntegerField(null=True)
    Subject=models.CharField(max_length=250)
    Student_photo=models.ImageField(upload_to='images/',null=True)