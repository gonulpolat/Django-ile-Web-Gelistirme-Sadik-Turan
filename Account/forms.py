from django import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets


class LoginUserForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if username == "admin":
            messages.add_message(self.request, messages.SUCCESS, 'Welcome admin')

        return username
    
    def confirm_login_allowed(self, user):

        if user.username.startswith("_"):
            raise forms.ValidationError("Username is not allowed")