from django.urls import path
from pen import views

urlpatterns = [
    path('', views.index, name='landing_page.html'),
    # path('signup/', views.SignupPage, name='signup'),
    # path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    # path('master_reg/', views.MasterReg, name='master_reg'),
    path('registration', views.registration,name='registration'),
    path('login', views.login_user,name='login'),
    path('coReg', views.coReg,name='master_reg'),

]