from django import forms
from django.contrib.auth.models import User
from .models import Supervisor
from apps.departments.models import Department


class SupervisorForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Password',
        required=False
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Supervisor
        fields = ['name', 'email', 'designation', 'department']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        supervisor = super().save(commit=False)
        if commit:
            # Create User if password provided
            if self.cleaned_data.get('password'):
                user = User.objects.create_user(
                    username=self.cleaned_data['email'],
                    email=self.cleaned_data['email'],
                    password=self.cleaned_data['password']
                )
                supervisor.user = user
            supervisor.save()
        return supervisor
