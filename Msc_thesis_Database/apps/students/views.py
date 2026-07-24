from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.accounts.decorators import admin_required, student_required
from .models import Student
from .forms import StudentForm


@admin_required
def student_list(request):
    """List all students."""
    students = Student.objects.select_related('department').all()
    return render(request, 'students/student_list.html', {'students': students})


@admin_required
def add_student(request):
    """Add a new student."""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student:list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm()

    return render(request, 'students/add_student.html', {'form': form})


@admin_required
def edit_student(request, pk):
    """Edit a student."""
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student:list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/edit_student.html', {'form': form, 'student': student})


@admin_required
def delete_student(request, pk):
    """Delete a student."""
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.user.delete()  # Deleting user also deletes student
        messages.success(request, 'Student deleted successfully!')
        return redirect('student:list')

    return render(request, 'students/delete_student.html', {'student': student})


@student_required
@login_required
def student_dashboard(request):
    """Student dashboard."""
    student = get_object_or_404(Student, user=request.user)
    from apps.theses.models import Thesis, Submission

    thesis = Thesis.objects.filter(student=student).first()
    submissions = Submission.objects.filter(thesis=thesis) if thesis else None

    if request.method == 'POST' and thesis:
        version = request.POST.get('version')
        thesis_file = request.FILES.get('thesis_file')

        if version:
            Submission.objects.create(
                thesis=thesis,
                version=version,
                thesis_file=thesis_file,
                approval_status='Pending'
            )
            messages.success(request, 'Submission created successfully!')
            return redirect('student:dashboard')
        else:
            messages.error(request, 'Please provide a version number.')

    context = {
        'student': student,
        'thesis': thesis,
        'submissions': submissions,
    }
    return render(request, 'student_dashboard.html', context)
