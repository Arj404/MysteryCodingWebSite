from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Register(UserCreationForm):
    email = forms.EmailField()
    roll_number = forms.IntegerField()
    name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'name', 'roll_number', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
