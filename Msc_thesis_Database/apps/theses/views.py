from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.accounts.decorators import admin_required, professor_required
from .models import Thesis, Evaluation, Submission, CommitteeMember, ThesisCommittee
from .forms import ThesisForm, EvaluationForm, SubmissionForm, CommitteeMemberForm


# ========== Thesis Views ==========

@admin_required
def thesis_list(request):
    """List all theses."""
    theses = Thesis.objects.select_related('student', 'supervisor').all()
    return render(request, 'theses/thesis_list.html', {'theses': theses})


@admin_required
def add_thesis(request):
    """Add a new thesis."""
    if request.method == 'POST':
        form = ThesisForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thesis added successfully!')
            return redirect('thesis:list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ThesisForm()

    return render(request, 'theses/add_thesis.html', {'form': form})


@admin_required
def edit_thesis(request, pk):
    """Edit a thesis."""
    thesis = get_object_or_404(Thesis, pk=pk)

    if request.method == 'POST':
        form = ThesisForm(request.POST, instance=thesis)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thesis updated successfully!')
            return redirect('thesis:list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ThesisForm(instance=thesis)

    return render(request, 'theses/edit_thesis.html', {'form': form, 'thesis': thesis})


@admin_required
def delete_thesis(request, pk):
    """Delete a thesis."""
    thesis = get_object_or_404(Thesis, pk=pk)

    if request.method == 'POST':
        thesis.delete()
        messages.success(request, 'Thesis deleted successfully!')
        return redirect('thesis:list')

    return render(request, 'theses/delete_thesis.html', {'thesis': thesis})


@admin_required
def view_thesis(request, pk):
    """View thesis details."""
    thesis = get_object_or_404(Thesis, pk=pk)
    submissions = thesis.submissions.all()
    evaluations = thesis.evaluations.all()
    committee_members = thesis.committee_members.all()

    context = {
        'thesis': thesis,
        'submissions': submissions,
        'evaluations': evaluations,
        'committee_members': committee_members,
    }
    return render(request, 'theses/view_thesis.html', context)


# ========== Evaluation Views ==========

@admin_required
def add_evaluation(request):
    """Add evaluation for a thesis."""
    theses = Thesis.objects.all()

    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evaluation added successfully!')
            return redirect('thesis:list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EvaluationForm()

    return render(request, 'theses/add_evaluation.html', {'form': form, 'theses': theses})


@admin_required
def edit_evaluation(request, pk):
    """Edit evaluation."""
    evaluation = get_object_or_404(Evaluation, pk=pk)

    if request.method == 'POST':
        form = EvaluationForm(request.POST, instance=evaluation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evaluation updated successfully!')
            return redirect('thesis:list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = EvaluationForm(instance=evaluation)

    return render(request, 'theses/edit_evaluation.html', {'form': form, 'evaluation': evaluation})


# ========== Submission Views ==========

@admin_required
def add_submission(request):
    """Add submission for a thesis."""
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submission added successfully!')
            return redirect('thesis:list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SubmissionForm()

    return render(request, 'theses/add_submission.html', {'form': form})


@admin_required
def submission_list(request):
    """List all submissions."""
    submissions = Submission.objects.select_related('thesis').all()
    return render(request, 'theses/submission_list.html', {'submissions': submissions})


# ========== Committee Member Views ==========

@admin_required
def committee_member_list(request):
    """List all committee members."""
    members = CommitteeMember.objects.all()
    return render(request, 'theses/committee_member_list.html', {'members': members})


@admin_required
def add_committee_member(request):
    """Add a committee member."""
    if request.method == 'POST':
        form = CommitteeMemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Committee member added successfully!')
            return redirect('thesis:committee_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CommitteeMemberForm()

    return render(request, 'theses/add_committee_member.html', {'form': form})


# ========== Admin Dashboard ==========

@admin_required
def admin_dashboard(request):
    """Admin dashboard showing statistics."""
    from apps.departments.models import Department
    from apps.students.models import Student
    from apps.supervisors.models import Supervisor

    context = {
        'departments': Department.objects.count(),
        'students': Student.objects.count(),
        'supervisors': Supervisor.objects.count(),
        'theses': Thesis.objects.count(),
        'evaluations': Evaluation.objects.count(),
        'submissions': Submission.objects.count(),
        'pending_theses': Thesis.objects.filter(status='Pending').count(),
    }
    return render(request, 'admin_dashboard.html', context)
