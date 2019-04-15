from django.shortcuts import render, redirect
from .form import Ans1, Ans2, Ans3
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def email(request):
    # form = Ans1()
    if request.method == 'POST':
        form = Ans1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Ans1()
    return render(request, 'day1/email_q1.html', {'ans': form})


@login_required
def story1(request):
    # form = Ans1()
    if request.method == 'POST':
        form = Ans1(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Ans1()
    return render(request, 'day1/story_before_q1.html', {'ans': form})

