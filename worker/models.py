from django.db import models
from django.conf import settings

class WorkerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='worker_profile')
    skills = models.TextField(blank=True, help_text="Comma separated skills, e.g. Carpentry, Masonry")
    experience_years = models.IntegerField(default=0)
    location = models.CharField(max_length=200, blank=True)
    is_available = models.BooleanField(default=True)
    daily_wage_expected = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} Profile"

class JobAssignment(models.Model):
    worker = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE, related_name='assignments')
    job = models.ForeignKey('client.JobRequirement', on_delete=models.CASCADE, related_name='assignments')
    status = models.CharField(max_length=20, default='ASSIGNED', choices=[
        ('ASSIGNED', 'Assigned'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled')
    ])
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.worker.user.username} assigned to {self.job.title}"
