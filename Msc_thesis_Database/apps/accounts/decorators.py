from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from .models import UserProfile


def role_required(*roles):
    """
    Decorator to require specific user roles.
    Usage: @role_required('admin', 'professor')
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.error(request, 'Please log in first.')
                return redirect('accounts:home')

            try:
                profile = UserProfile.objects.get(user=request.user)
                if profile.role in roles:
                    return view_func(request, *args, **kwargs)
                else:
                    messages.error(request, 'You do not have permission to access this page.')
                    return redirect('accounts:home')
            except UserProfile.DoesNotExist:
                messages.error(request, 'User profile not found.')
                return redirect('accounts:home')

        return wrapper
    return decorator


def admin_required(view_func):
    """Decorator to require admin role."""
    return role_required('admin')(view_func)


def professor_required(view_func):
    """Decorator to require professor role."""
    return role_required('professor')(view_func)


def student_required(view_func):
    """Decorator to require student role."""
    return role_required('student')(view_func)
