from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def manager_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_manager_user():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied("You do not have permission to access the NGO Command Dashboard.")
    return _wrapped_view

@manager_required
def dashboard_view(request):
    context = {
        'total_workers': 45,
        'deployed_workers': 28,
        'pending_requests': 7,
        'active_clients': 12,
    }
    return render(request, 'manager/dashboard.html', context)
