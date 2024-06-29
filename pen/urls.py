from django.urls import path
from . import views
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_user, name='login'),
    path('coReg/', views.coReg, name='coReg'),



    
    path('submit_writing/', views.submit_writing, name='submit_writing'),
    path('check-content/<int:submission_id>/', views.check_content, name='check_content'),
    path('accept_submission/<int:submission_id>/', views.accept_submission, name='accept_submission'),
    path('view_submissions/', views.view_submissions,name='view_submissions'),
    path('evaluation_page/', views.evaluation_page, name='evaluation_page'),
    path('read-file-content/<int:submission_id>/', views.read_file_content, name='read_file_content'),
    path('submission_status/', views.submission_status, name='submission_status'),
    path('accept/<int:submission_id>/', views.accept_submission, name='accept_submission'),
    path('save_feedback/<int:submission_id>/', views.save_feedback, name='save_feedback'),
    path('submission_history/', views.submission_history, name='submission_history'),
    path('subm_his_user/', views.subm_his_user, name='subm_his_user'),
    


    path('adminmaster/', views.adminmaster,name='adminmaster'),
    path('approvemaster', views.approvemaster,name='approvemaster'),
    path('admin_master_view', views.admin_master_view,name='admin_master_view'),
    # path main folder latest version 1.1
]
