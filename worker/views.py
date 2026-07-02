from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def worker_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_worker_user():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied("You do not have permission to access the Employee Console.")
    return _wrapped_view

@worker_required
def dashboard_view(request):
    from .models import WorkerProfile, JobAssignment
    try:
        profile = request.user.worker_profile
    except WorkerProfile.DoesNotExist:
        profile = None
    
    active_assignment = None
    if profile:
        active_assignment = JobAssignment.objects.filter(worker=profile, status='ASSIGNED').first()
        
    context = {
        'profile': profile,
        'active_assignment': active_assignment,
    }
    return render(request, 'worker/dashboard.html', context)

@worker_required
def my_assignments_view(request):
    from .models import WorkerProfile, JobAssignment
    try:
        profile = request.user.worker_profile
        assignments = JobAssignment.objects.filter(worker=profile).select_related('job', 'job__employer').order_by('-assigned_at')
    except WorkerProfile.DoesNotExist:
        assignments = []
        
    return render(request, 'worker/my_assignments.html', {'assignments': assignments})

@worker_required
def attendance_view(request):
    # Mock attendance logs
    logs = [
        {'date': '2026-06-30', 'check_in': '08:58 AM', 'check_out': '06:05 PM', 'status': 'Present'},
        {'date': '2026-06-29', 'check_in': '08:55 AM', 'check_out': '06:00 PM', 'status': 'Present'},
        {'date': '2026-06-28', 'check_in': '09:02 AM', 'check_out': '06:10 PM', 'status': 'Present'},
    ]
    return render(request, 'worker/attendance.html', {'logs': logs})

@worker_required
def support_view(request):
    if request.method == 'POST':
        messages.success(request, "Your query has been submitted. A coordinator will contact you on your registered phone number.")
        return redirect('worker:dashboard')
    return render(request, 'worker/support.html')
