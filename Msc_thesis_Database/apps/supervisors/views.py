from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.accounts.decorators import admin_required, professor_required
from .models import Supervisor
from .forms import SupervisorForm


@admin_required
def supervisor_list(request):
    """List all supervisors."""
    supervisors = Supervisor.objects.select_related('department').all()
    return render(request, 'supervisors/supervisor_list.html', {'supervisors': supervisors})


@admin_required
def add_supervisor(request):
    """Add a new supervisor."""
    if request.method == 'POST':
        form = SupervisorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supervisor added successfully!')
            return redirect('supervisor:list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SupervisorForm()

    return render(request, 'supervisors/add_supervisor.html', {'form': form})


@admin_required
def edit_supervisor(request, pk):
    """Edit a supervisor."""
    supervisor = get_object_or_404(Supervisor, pk=pk)

    if request.method == 'POST':
        form = SupervisorForm(request.POST, instance=supervisor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supervisor updated successfully!')
            return redirect('supervisor:list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SupervisorForm(instance=supervisor)

    return render(request, 'supervisors/edit_supervisor.html', {'form': form, 'supervisor': supervisor})


@admin_required
def delete_supervisor(request, pk):
    """Delete a supervisor."""
    supervisor = get_object_or_404(Supervisor, pk=pk)

    if request.method == 'POST':
        if supervisor.user:
            supervisor.user.delete()  # Deleting user also deletes supervisor
        else:
            supervisor.delete()
        messages.success(request, 'Supervisor deleted successfully!')
        return redirect('supervisor:list')

    return render(request, 'supervisors/delete_supervisor.html', {'supervisor': supervisor})


@professor_required
@login_required
def supervisor_dashboard(request):
    """Supervisor/Professor dashboard."""
    supervisor = get_object_or_404(Supervisor, user=request.user)
    from apps.theses.models import Thesis

    theses = Thesis.objects.filter(supervisor=supervisor).select_related('student')

    total = theses.count()
    pending = theses.filter(status='Pending').count()
    approved = theses.filter(status='Approved').count()
    rejected = theses.filter(status='Rejected').count()

    context = {
        'supervisor': supervisor,
        'theses': theses,
        'total': total,
        'pending': pending,
        'approved': approved,
        'rejected': rejected,
    }

    return render(request, 'prof_dashboard.html', context)
