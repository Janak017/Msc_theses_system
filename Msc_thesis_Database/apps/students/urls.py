from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.student_list, name='list'),
    path('add/', views.add_student, name='add'),
    path('<int:pk>/edit/', views.edit_student, name='edit'),
    path('<int:pk>/delete/', views.delete_student, name='delete'),
    path('dashboard/', views.student_dashboard, name='dashboard'),
]
