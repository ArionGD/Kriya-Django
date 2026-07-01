from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('workers/', views.workers_list_view, name='workers_list'),
    path('clients/', views.client_audits_view, name='client_audits'),
    path('settings/', views.settings_view, name='settings'),
]
