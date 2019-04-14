from django.shortcuts import render

# Create your views here.


def email(request):
    return render(request, 'day1/email_q1.html')


def story1(request):
    return render(request, 'day1/story_before_q1.html')

