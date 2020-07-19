from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginP, name=""),
    path('index', views.loginP, name="index"),
    path('main', views.mainpage, name="main"),
    path('searchResult', views.searchResult, name="searhResult"),
    path('jobs_list', views.jobsList, name="searhResult"),
    path('job_details/<int:jobid>', views.jobDetails, name="job_details"),
    path('job_details/job_application/<int:jobid>', views.applicationForm, name="applicationForm"),
    path('register', views.register, name="register"),
    path('myjobs', views.myJobs, name="myJobs"),
    path('addJob', views.addJob, name="addJob"),
    path('addJobForm', views.addJobForm, name="addJobForm"),
    path('registerUser', views.addUser, name="addUser"),
    path('loginUser', views.loginCheck, name="loginCheck"),
    path('logoutUser', views.logoutUser, name="logoutUser"),
    path('delJob/<int:jobid>', views.delJob, name="delJob"),
    path('editjob/<int:jobid>', views.editjob, name="editjob"),
    path('editjob/myjobs', views.backtoMyJobs, name="backtoMyJobs"),
    path('editjob/main', views.reMain, name="reMain"),
    path('editjob/confirmedit/<int:jobid>', views.confirmedit, name="confirmedit"),
    path('job_details/<str:whereto>', views.redirector, name = "redirector"),
    path('job_details/job_application/<str:whereto>', views.applyRedirector, name = "applyRedirector"),
]