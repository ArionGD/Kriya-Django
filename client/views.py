from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import JobRequirement
from .forms import JobRequirementForm

def client_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_client_user():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied("You do not have permission to access the Employer Console.")
    return _wrapped_view

@client_required
def dashboard_view(request):
    requirements = JobRequirement.objects.filter(employer=request.user).order_by('-created_at')
    context = {
        'requirements': requirements,
        'active_requests': requirements.filter(status='PENDING').count(),
        'fulfilled_requests': requirements.filter(status='MATCHED').count(),
        'deployed_count': 14, # Mock stat
    }
    return render(request, 'client/dashboard.html', context)

@client_required
def post_requirement_view(request):
    if request.method == 'POST':
        form = JobRequirementForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.employer = request.user
            req.save()
            messages.success(request, "Staffing requirement posted successfully! The Kriya matching engine will match employees shortly.")
            return redirect('client:dashboard')
    else:
        form = JobRequirementForm()
    return render(request, 'client/post_requirement.html', {'form': form})

@client_required
def active_staff_view(request):
    # Mock data for demonstration
    active_staff = [
        {'name': 'Ravi Chandran', 'vocation': 'Mason', 'site': 'Chennai Central', 'status': 'Working'},
        {'name': 'Aditya Kumar', 'vocation': 'Welder', 'site': 'Chennai North', 'status': 'Working'},
    ]
    return render(request, 'client/active_staff.html', {'active_staff': active_staff})

@client_required
def settings_view(request):
    return render(request, 'client/settings.html')
