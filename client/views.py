from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def client_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_client_user():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied("You do not have permission to access the Client Console.")
    return _wrapped_view

@client_required
def dashboard_view(request):
    context = {
        'active_requests': 3,
        'fulfilled_requests': 5,
        'deployed_count': 14,
    }
    return render(request, 'client/dashboard.html', context)
