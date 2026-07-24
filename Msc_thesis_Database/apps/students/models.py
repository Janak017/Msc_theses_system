from django.db import models
from django.contrib.auth.models import User
from apps.departments.models import Department


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    batch = models.CharField(max_length=20)
    program = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['name']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['batch']),
        ]

    def __str__(self):
        return self.name
