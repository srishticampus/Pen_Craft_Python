from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserReg,Master

admin.site.register(UserReg)
admin.site.register(Master)
