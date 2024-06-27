from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserReg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    location = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_images/',blank=True,null=True)

    def __str__(self):
        return self.user.username
    