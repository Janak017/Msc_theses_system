from django.contrib import admin
from .models import Thesis, Evaluation, Submission, CommitteeMember, ThesisCommittee


@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = ('title', 'student', 'supervisor', 'status', 'submission_year', 'created_at')
    list_filter = ('status', 'submission_year', 'created_at')
    search_fields = ('title', 'student__name', 'supervisor__name')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('thesis', 'marks', 'result', 'evaluation_date', 'evaluated_by')
    list_filter = ('result', 'evaluation_date')
    search_fields = ('thesis__title', 'evaluated_by')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('thesis', 'version', 'approval_status', 'submission_date')
    list_filter = ('approval_status', 'submission_date')
    search_fields = ('thesis__title',)
    readonly_fields = ('created_at', 'updated_at', 'submission_date')


@admin.register(CommitteeMember)
class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'department')
    search_fields = ('name', 'department')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ThesisCommittee)
class ThesisCommitteeAdmin(admin.ModelAdmin):
    list_display = ('thesis', 'member')
    list_filter = ('thesis',)
    search_fields = ('thesis__title', 'member__name')
