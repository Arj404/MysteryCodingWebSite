from django.shortcuts import render, redirect
from .form import Register
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def form(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} registered')
            return redirect('login')
    else:
        form = Register()
    return render(request, 'registration/register.html', {'form': form})


def index(request):
    return render(request, 'index/index.html')


@login_required
def instruction(request):
    return render(request, 'index/instruction.html')
