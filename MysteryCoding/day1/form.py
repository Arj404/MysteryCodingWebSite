from django import forms
from .models import *
from django.contrib.auth.forms import User


class Ans1(forms.ModelForm):
    ans = forms.FileField(required=True)
    def save(self, commit=False):
        answer = super(Ans1, self).save(commit=False)
        answer.ans = self.cleaned_data['ans']
        if commit:
            answer.save()
        return answer
    class Meta:
        model = Day11
        fields = ('ans',)
        exclude = ('user',)


class Answer(forms.ModelForm):
    class Meta:
        model = Day
        exclude = ('author',)

    def clean_answer(self):
        if not self.cleaned_data['author']:
            return User
        return self.cleaned_data['author']


class Ans2(forms.ModelForm):
    class Meta:
        model = Day12
        fields = ['ans1_2']
    def __unicode__(self):
        return self.name


class Ans3(forms.ModelForm):
    class Meta:
        model = Day13
        fields = ['ans1_3']
    def __unicode__(self):
        return self.name

