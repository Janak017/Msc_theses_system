"""
Common utility functions for the thesis system.
"""


def format_file_size(bytes_size):
    """Format bytes to human readable file size."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.1f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.1f} TB"


def get_user_role(user):
    """Get the role of a user."""
    try:
        return user.profile.role
    except AttributeError:
        return None


def is_user_role(user, role):
    """Check if user has a specific role."""
    try:
        return user.profile.role == role
    except AttributeError:
        return False
