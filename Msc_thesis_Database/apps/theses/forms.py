from django import forms
from .models import Thesis, Evaluation, Submission, CommitteeMember, ThesisCommittee
from apps.students.models import Student
from apps.supervisors.models import Supervisor


class ThesisForm(forms.ModelForm):
    class Meta:
        model = Thesis
        fields = ['title', 'abstract', 'submission_year', 'status', 'student', 'supervisor']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'abstract': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'submission_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'student': forms.Select(attrs={'class': 'form-control'}),
            'supervisor': forms.Select(attrs={'class': 'form-control'}),
        }


class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['marks', 'result', 'feedback', 'evaluated_by']
        widgets = {
            'marks': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'result': forms.Select(attrs={'class': 'form-control'}),
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'evaluated_by': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['thesis', 'version', 'approval_status', 'thesis_file']
        widgets = {
            'thesis': forms.Select(attrs={'class': 'form-control'}),
            'version': forms.NumberInput(attrs={'class': 'form-control'}),
            'approval_status': forms.Select(attrs={'class': 'form-control'}),
            'thesis_file': forms.FileInput(attrs={'class': 'form-control'}),
        }


class CommitteeMemberForm(forms.ModelForm):
    class Meta:
        model = CommitteeMember
        fields = ['name', 'role', 'department']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
        }
