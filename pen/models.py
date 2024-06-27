from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserReg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='example@example.com')
    image = models.ImageField(upload_to='Profile', default='profile/default.jpg')
    qualification = models.CharField(max_length=100,default='Not Provided')
    phone_number = models.CharField(max_length=20,default='Not Provided')
    address = models.CharField(max_length=255,default='Not Provided')
    location = models.CharField(max_length=100,default='Not Provided')
    state = models.CharField(max_length=100,default='Not Provided')
    city = models.CharField(max_length=100,default='Not Provided')

    def __str__(self):
        return self.user.username
    

class Master(models.Model):
    name = models.CharField(max_length=50,default='Not Provided')
    email = models.EmailField(default='example@example.com')
    phone = models.CharField(max_length=50,default='Not Provided')
    address = models.CharField(max_length=50)
    qual = models.CharField(max_length=50)
    field = models.CharField(max_length=50,default='Default Value')
    img = models.ImageField(upload_to='Profile')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
