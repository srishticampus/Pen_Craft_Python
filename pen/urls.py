from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_user, name='login'),
    path('coReg/', views.coReg, name='coReg'),
#     path('adminmaster/', views.adminmaster,name='adminmaster'),
#     path('approvemaster', views.approvemaster,name='approvemaster'),
]
