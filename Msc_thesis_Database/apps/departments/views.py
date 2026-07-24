from django.shortcuts import render, redirect
from django.contrib import messages
from apps.accounts.decorators import admin_required
from .models import Department
from .forms import DepartmentForm


@admin_required
def department_list(request):
    """List all departments."""
    departments = Department.objects.all()
    return render(request, 'departments/department_list.html', {'departments': departments})


@admin_required
def add_department(request):
    """Add a new department."""
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department added successfully!')
            return redirect('department:list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = DepartmentForm()

    return render(request, 'departments/add_department.html', {'form': form})


@admin_required
def edit_department(request, pk):
    """Edit a department."""
    department = Department.objects.get(pk=pk)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department updated successfully!')
            return redirect('department:list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'departments/edit_department.html', {'form': form, 'department': department})


@admin_required
def delete_department(request, pk):
    """Delete a department."""
    department = Department.objects.get(pk=pk)

    if request.method == 'POST':
        department.delete()
        messages.success(request, 'Department deleted successfully!')
        return redirect('department:list')

    return render(request, 'departments/delete_department.html', {'department': department})
