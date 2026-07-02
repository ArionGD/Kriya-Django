from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('features/', views.features_view, name='features'),
    path('support/', views.support_view, name='support'),
    path('help/', views.help_guide_view, name='help_guide'),
]
