from django.urls import path
from . import views

urlpatterns = [
    path('adminmaster/', views.adminmaster, name='adminmaster'),
    path('approvemaster', views.approvemaster, name='approvemaster'),
]
