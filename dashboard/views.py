from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def role_required(role_check_func):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if role_check_func(request.user):
                return view_func(request, *args, **kwargs)
            raise PermissionDenied("You do not have permission to access this page.")
        return _wrapped_view
    return decorator

@role_required(lambda u: u.is_manager_user())
def ngo_dashboard_view(request):
    # Dummy stats for the prototype showcase
    context = {
        'total_workers': 45,
        'deployed_workers': 28,
        'pending_requests': 7,
        'active_clients': 12,
    }
    return render(request, 'dashboard/ngo.html', context)

@role_required(lambda u: u.is_client_user())
def client_dashboard_view(request):
    # Dummy stats for the prototype showcase
    context = {
        'active_requests': 3,
        'fulfilled_requests': 5,
        'deployed_count': 14,
    }
    return render(request, 'dashboard/client.html', context)

@role_required(lambda u: u.is_worker_user())
def worker_dashboard_view(request):
    # Dummy info for the worker
    context = {
        'worker_status': 'Ready for Placement',
        'current_job': 'None',
        'training_completed': True,
    }
    return render(request, 'dashboard/worker.html', context)

