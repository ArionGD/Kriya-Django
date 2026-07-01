from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('post-requirement/', views.post_requirement_view, name='post_requirement'),
    path('active-staff/', views.active_staff_view, name='active_staff'),
    path('settings/', views.settings_view, name='settings'),
]
