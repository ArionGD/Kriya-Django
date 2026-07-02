from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('program/', views.program_view, name='program'),
    path('support/', views.support_view, name='support'),
]
