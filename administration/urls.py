from django.urls import path
from administration import views

urlpatterns = [
    path('login',views.LoginPage,name='login.html'),
    path('dash',views.index,name='admin_dashboard.html'),
    path('submit_writing/', views.submit_writing, name='submit_writing'),
    path('submission_success/', views.submission_success, name='submission_success'),
    path('submission_history/', views.submission_history, name='submission_history'), 
    path('submission_detail/<int:submission_id>/', views.submission_detail, name='submission_detail'),


    


]
