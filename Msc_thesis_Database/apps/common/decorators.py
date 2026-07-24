from django.shortcuts import redirect
from django.contrib import messages


def require_ajax(view_func):
    """Decorator to require AJAX requests only."""
    def wrapper(request, *args, **kwargs):
        if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            messages.error(request, 'Invalid request.')
            return redirect('accounts:home')
        return view_func(request, *args, **kwargs)
    return wrapper
