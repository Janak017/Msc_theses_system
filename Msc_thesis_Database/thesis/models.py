from django.db import models
from django.contrib.auth.models import User

# UserProfile
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('professor', 'Professor'),
        ('student', 'Student')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"


# Departments
class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100)
    office_location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.department_name


# Students
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    batch = models.CharField(max_length=20)
    program = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name


# Supervisors
class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    supervisor_id = models.AutoField(primary_key=True)
    supervisor_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.supervisor_name


# Thesis
class Thesis(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    )

    thesis_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    submission_year = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Evaluation
class Evaluation(models.Model):
    evaluation_id = models.AutoField(primary_key=True)
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)
    evaluation_date = models.DateField(auto_now_add=True)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    result = models.CharField(max_length=20)

    def __str__(self):
        return f"Evaluation {self.evaluation_id} - {self.thesis.title}"


# Committee Members
class CommitteeMember(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.member_name


# Submissions
class Submission(models.Model):
    APPROVAL_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    )

    submission_id = models.AutoField(primary_key=True)
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)
    submission_date = models.DateField(auto_now_add=True)
    version = models.IntegerField()
    approval_status = models.CharField(max_length=50, choices=APPROVAL_CHOICES)
    thesis_file = models.FileField(upload_to='thesis_files/', null=True, blank=True)

    def __str__(self):
        return f"{self.thesis.title} - v{self.version}"


# Thesis Committee
class ThesisCommittee(models.Model):
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)
    member = models.ForeignKey(CommitteeMember, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('thesis', 'member')

    def __str__(self):
        return f"{self.thesis.title} - {self.member.member_name}"


# Admin convenience ManyToMany
Thesis.add_to_class(
    'committee_members',
    models.ManyToManyField(CommitteeMember, through='ThesisCommittee')
)