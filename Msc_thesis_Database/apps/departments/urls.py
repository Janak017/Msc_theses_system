from django.urls import path
from . import views

app_name = 'department'

urlpatterns = [
    path('', views.department_list, name='list'),
    path('add/', views.add_department, name='add'),
    path('<int:pk>/edit/', views.edit_department, name='edit'),
    path('<int:pk>/delete/', views.delete_department, name='delete'),
]
