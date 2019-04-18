from django.shortcuts import render, redirect
from .form import *
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def email(request):
    print("test1")
    if request.method == "POST":
        form = Answer(request.POST ,instance=request.user)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            form.save()
            return redirect('/')
        else:
            print("error")
    else:
        form = Answer()
    return render(request, 'day1/email_q1.html', {'ans1_1': form})




@login_required
def story1(request):

    return render(request, 'day1/story_before_q1.html')


@login_required
def ip(request):
    return render(request, 'day1/ip.html')

@login_required
def riddle(request):
    return render(request, 'day1/riddle_q2.html')

