from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        SUPERUSER = 'SUPERUSER', 'Superuser'
        MANAGER = 'MANAGER', 'NGO Manager'
        CLIENT = 'CLIENT', 'Client / Recruiter'
        WORKER = 'WORKER', 'Worker'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.WORKER
    )

    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def is_manager_user(self):
        return self.role == self.Role.MANAGER or self.is_superuser

    def is_client_user(self):
        return self.role == self.Role.CLIENT

    def is_worker_user(self):
        return self.role == self.Role.WORKER

    def save(self, *args, **kwargs):
        # Automatically set role to SUPERUSER if created as superuser
        if self.is_superuser and self.role != self.Role.SUPERUSER:
            self.role = self.Role.SUPERUSER
        super().save(*args, **kwargs)

