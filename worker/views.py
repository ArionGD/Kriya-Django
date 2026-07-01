from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def worker_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_worker_user():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied("You do not have permission to access the Worker Console.")
    return _wrapped_view

@worker_required
def dashboard_view(request):
    context = {
        'worker_status': 'Ready for Placement',
        'current_job': 'None',
        'training_completed': True,
    }
    return render(request, 'worker/dashboard.html', context)
