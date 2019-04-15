from django import forms
from day1.models import Day11, Day12, Day13
from django.contrib.auth.forms import User


class Ans1(forms.Form):
    # Enter_your_discovery = forms.CharField(max_length=10)
    class Meta:
        model = Day11
        fields = ['ans1_1']


class Ans2(forms.ModelForm):
    class Meta:
        model = Day12
        fields = ['ans1_2']


class Ans3(forms.ModelForm):
    class Meta:
        model = Day13
        fields = ['ans1_3']

