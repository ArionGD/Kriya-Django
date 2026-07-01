from django.urls import path
from . import views

app_name = 'worker'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('assignments/', views.my_assignments_view, name='my_assignments'),
    path('attendance/', views.attendance_view, name='attendance'),
    path('support/', views.support_view, name='support'),
]
