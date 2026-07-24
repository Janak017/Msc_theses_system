from django.urls import path
from . import views

app_name = 'supervisor'

urlpatterns = [
    path('', views.supervisor_list, name='list'),
    path('add/', views.add_supervisor, name='add'),
    path('<int:pk>/edit/', views.edit_supervisor, name='edit'),
    path('<int:pk>/delete/', views.delete_supervisor, name='delete'),
    path('dashboard/', views.supervisor_dashboard, name='dashboard'),
]
