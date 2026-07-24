from django.db import models
from apps.students.models import Student
from apps.supervisors.models import Supervisor


class Thesis(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    title = models.CharField(max_length=255)
    abstract = models.TextField()
    submission_year = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='thesis')
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, related_name='theses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Thesis'
        verbose_name_plural = 'Theses'
        ordering = ['-submission_year', 'title']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['submission_year']),
        ]

    def __str__(self):
        return self.title


class CommitteeMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Committee Member'
        verbose_name_plural = 'Committee Members'
        ordering = ['name']

    def __str__(self):
        return self.name


class ThesisCommittee(models.Model):
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE, related_name='committee_members')
    member = models.ForeignKey(CommitteeMember, on_delete=models.CASCADE, related_name='thesis_assignments')

    class Meta:
        unique_together = ('thesis', 'member')
        verbose_name = 'Thesis Committee'
        verbose_name_plural = 'Thesis Committees'

    def __str__(self):
        return f"{self.thesis.title} - {self.member.name}"


class Submission(models.Model):
    APPROVAL_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE, related_name='submissions')
    submission_date = models.DateField(auto_now_add=True)
    version = models.IntegerField()
    approval_status = models.CharField(max_length=50, choices=APPROVAL_CHOICES)
    thesis_file = models.FileField(upload_to='thesis_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Submission'
        verbose_name_plural = 'Submissions'
        ordering = ['-submission_date', '-version']
        indexes = [
            models.Index(fields=['approval_status']),
        ]

    def __str__(self):
        return f"{self.thesis.title} - v{self.version}"


class Evaluation(models.Model):
    RESULT_CHOICES = (
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('Pending', 'Pending'),
    )

    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE, related_name='evaluations')
    evaluation_date = models.DateField(auto_now_add=True)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    result = models.CharField(max_length=20, choices=RESULT_CHOICES)
    feedback = models.TextField(blank=True, null=True)
    evaluated_by = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Evaluation'
        verbose_name_plural = 'Evaluations'
        ordering = ['-evaluation_date']

    def __str__(self):
        return f"Evaluation {self.id} - {self.thesis.title}"
