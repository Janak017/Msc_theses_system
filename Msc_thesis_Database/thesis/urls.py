from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('prof_login/', views.prof_login, name='prof_login'),
    path('prof_dashboard/', views.prof_dashboard, name='prof_dashboard'),

    path('student_login/', views.student_login, name='student_login'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),

    path("add_department/", views.add_department, name="add_department"),
    path("add_student/", views.add_student, name="add_student"),
    path("add_supervisor/", views.add_supervisor, name="add_supervisor"),
    path("add_thesis/", views.add_thesis, name="add_thesis"),
    path("add_evaluation/", views.add_evaluation, name="add_evaluation"),
    path("add_submission/", views.add_submission, name="add_submission"),

    path('logout/', views.home, name='logout'),
]