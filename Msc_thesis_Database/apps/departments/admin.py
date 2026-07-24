from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'office_location', 'created_at')
    search_fields = ('name', 'office_location')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('name',)
