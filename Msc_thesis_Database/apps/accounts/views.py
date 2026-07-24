from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def home(request):
    """Home page view."""
    return render(request, 'home.html')


def login_view(request, role='student'):
    """
    Generic login view for different user roles.
    Supports 'student', 'professor', and 'admin' roles.
    """
    if request.user.is_authenticated:
        profile = request.user.profile
        if profile.role == 'student':
            return redirect('student:dashboard')
        elif profile.role == 'professor':
            return redirect('supervisor:dashboard')
        elif profile.role == 'admin':
            return redirect('admin:dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                try:
                    profile = user.profile
                    if profile.role == role or role == 'all':
                        login(request, user)
                        messages.success(request, f'Welcome, {user.first_name or username}!')

                        # Redirect based on role
                        if profile.role == 'student':
                            return redirect('student:dashboard')
                        elif profile.role == 'professor':
                            return redirect('supervisor:dashboard')
                        elif profile.role == 'admin':
                            return redirect('admin:dashboard')
                    else:
                        messages.error(request, f'Invalid role. You are registered as a {profile.get_role_display().lower()}.')
                except AttributeError:
                    messages.error(request, 'User profile not found. Please contact administrator.')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please check your input and try again.')

    else:
        form = LoginForm()

    template = f'{role}_login.html' if role != 'all' else 'login.html'
    return render(request, template, {'form': form})


def student_login(request):
    """Student login view."""
    return login_view(request, role='student')


def professor_login(request):
    """Professor/Supervisor login view."""
    return login_view(request, role='professor')


def admin_login(request):
    """Admin login view."""
    return login_view(request, role='admin')


@login_required(login_url='accounts:student_login')
def logout_view(request):
    """Logout view."""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('accounts:home')
