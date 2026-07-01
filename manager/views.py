from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from accounts.models import User

def manager_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_manager_user():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied("You do not have permission to access the NGO Command Dashboard.")
    return _wrapped_view

@manager_required
def dashboard_view(request):
    employees = User.objects.filter(role=User.Role.WORKER)
    employers = User.objects.filter(role=User.Role.CLIENT)
    context = {
        'total_workers': employees.count(),
        'deployed_workers': 28, # Mock
        'pending_requests': 7,  # Mock
        'active_clients': employers.count(),
    }
    return render(request, 'manager/dashboard.html', context)

@manager_required
def workers_list_view(request):
    employees = User.objects.filter(role=User.Role.WORKER).order_by('username')
    return render(request, 'manager/workers_list.html', {'employees': employees})

@manager_required
def client_audits_view(request):
    employers = User.objects.filter(role=User.Role.CLIENT).order_by('username')
    return render(request, 'manager/client_audits.html', {'employers': employers})

@manager_required
def settings_view(request):
    return render(request, 'manager/settings.html')
