from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('ngo/', views.ngo_dashboard_view, name='ngo_dashboard'),
    path('client/', views.client_dashboard_view, name='client_dashboard'),
    path('worker/', views.worker_dashboard_view, name='worker_dashboard'),
]
