from django.urls import path
from pen import views

urlpatterns = [
     path('',views.index,name='landing_page.html'),

    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),


]
