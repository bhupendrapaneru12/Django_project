from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    is_student=models.BooleanField()
    email=models.EmailField()
    message=models.TextField()
    photo=models.ImageField(upload_to='image',null=True, blank=True)


class user_table(models.Model):
    name = models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='image',null=True, blank=True)