from django import forms
from index.models import login


class Register(forms.ModelForm):
    class Meta:
        model = login
        fields = ('name', 'roll_number', 'email', 'password')
