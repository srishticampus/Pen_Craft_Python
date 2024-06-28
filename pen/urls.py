from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_user, name='login'),
    path('coReg/', views.coReg, name='coReg'),



    path('view_submissions/', views.view_submissions,name='view_submissions'),
    path('submit_writing/', views.submit_writing, name='submit_writing'),



    path('adminmaster/', views.adminmaster,name='adminmaster'),
    path('approvemaster', views.approvemaster,name='approvemaster'),
    path('admin_master_view', views.admin_master_view,name='admin_master_view'),
]
