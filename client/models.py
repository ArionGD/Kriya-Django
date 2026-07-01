from django.db import models
from django.conf import settings

class JobRequirement(models.Model):
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    workers_needed = models.IntegerField(default=1)
    daily_wage = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200)
    provides_housing = models.BooleanField(default=False)
    provides_meals = models.BooleanField(default=False)
    provides_medical = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='PENDING', choices=[
        ('PENDING', 'Pending Match'),
        ('MATCHED', 'Matched'),
        ('CANCELLED', 'Cancelled')
    ])

    def __str__(self):
        return f"{self.title} ({self.workers_needed} needed)"

