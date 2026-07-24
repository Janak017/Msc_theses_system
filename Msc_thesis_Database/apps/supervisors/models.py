from django.db import models
from django.contrib.auth.models import User
from apps.departments.models import Department


class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='supervisor_profile', blank=True, null=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='supervisors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Supervisor'
        verbose_name_plural = 'Supervisors'
        ordering = ['name']
        indexes = [
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return self.name
