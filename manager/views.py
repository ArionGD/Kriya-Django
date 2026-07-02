from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from accounts.models import User
from worker.models import WorkerProfile, JobAssignment
from client.models import JobRequirement
from .forms import WorkerRegistrationForm

def manager_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_manager_user():
            return view_func(request, *args, **kwargs)
        raise PermissionDenied("You do not have permission to access the NGO Command Dashboard.")
    return _wrapped_view

@manager_required
def dashboard_view(request):
    total_workers = WorkerProfile.objects.count()
    available_workers = WorkerProfile.objects.filter(is_available=True).count()
    active_jobs = JobRequirement.objects.filter(status='PENDING').count()
    total_placements = JobAssignment.objects.count()
    
    recent_jobs = JobRequirement.objects.order_by('-created_at')[:5]
    recent_workers = WorkerProfile.objects.order_by('-user__date_joined')[:5]

    context = {
        'total_workers': total_workers,
        'available_workers': available_workers,
        'active_jobs': active_jobs,
        'total_placements': total_placements,
        'recent_jobs': recent_jobs,
        'recent_workers': recent_workers,
    }
    return render(request, 'manager/dashboard.html', context)

@manager_required
def register_worker_view(request):
    if request.method == 'POST':
        form = WorkerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Worker registered successfully!')
            return redirect('manager:workers_list')
    else:
        form = WorkerRegistrationForm()
    
    return render(request, 'manager/register_worker.html', {'form': form})

@manager_required
def job_matching_view(request, job_id):
    job = get_object_or_404(JobRequirement, id=job_id)
    available_workers = WorkerProfile.objects.filter(is_available=True)
    
    if request.method == 'POST':
        worker_id = request.POST.get('worker_id')
        if worker_id:
            worker = get_object_or_404(WorkerProfile, id=worker_id)
            JobAssignment.objects.create(worker=worker, job=job)
            worker.is_available = False
            worker.save()
            
            # Check if job requirement is met
            assigned_count = job.assignments.count()
            if assigned_count >= job.workers_needed:
                job.status = 'MATCHED'
                job.save()
            
            messages.success(request, f'Worker {worker.user.username} assigned to job {job.title}.')
            return redirect('manager:job_matching', job_id=job.id)
            
    context = {
        'job': job,
        'available_workers': available_workers,
        'assignments': job.assignments.all()
    }
    return render(request, 'manager/job_matching.html', context)

@manager_required
def workers_list_view(request):
    workers = WorkerProfile.objects.select_related('user').order_by('user__username')
    return render(request, 'manager/workers_list.html', {'workers': workers})

@manager_required
def client_audits_view(request):
    employers = User.objects.filter(role=User.Role.CLIENT).order_by('username')
    return render(request, 'manager/client_audits.html', {'employers': employers})

@manager_required
def settings_view(request):
    return render(request, 'manager/settings.html')
