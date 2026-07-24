from django.urls import path
from . import views

app_name = 'thesis'

urlpatterns = [
    # Admin Dashboard
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Thesis URLs
    path('', views.thesis_list, name='list'),
    path('add/', views.add_thesis, name='add'),
    path('<int:pk>/', views.view_thesis, name='detail'),
    path('<int:pk>/edit/', views.edit_thesis, name='edit'),
    path('<int:pk>/delete/', views.delete_thesis, name='delete'),

    # Evaluation URLs
    path('evaluation/add/', views.add_evaluation, name='add_evaluation'),
    path('evaluation/<int:pk>/edit/', views.edit_evaluation, name='edit_evaluation'),

    # Submission URLs
    path('submission/add/', views.add_submission, name='add_submission'),
    path('submissions/', views.submission_list, name='submissions'),

    # Committee Member URLs
    path('committee/', views.committee_member_list, name='committee_list'),
    path('committee/add/', views.add_committee_member, name='add_committee'),
]
