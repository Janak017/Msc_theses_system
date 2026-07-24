from django.contrib import admin
from .models import Supervisor


@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'designation', 'department', 'created_at')
    list_filter = ('designation', 'department', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('name',)
