from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('workers/', views.workers_list_view, name='workers_list'),
    path('register-worker/', views.register_worker_view, name='register_worker'),
    path('job-matching/<int:job_id>/', views.job_matching_view, name='job_matching'),
    path('clients/', views.client_audits_view, name='client_audits'),
    path('settings/', views.settings_view, name='settings'),
]
