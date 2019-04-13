from django.shortcuts import render, redirect
from .form import Register
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} registered')
            return redirect('login')
    else:
        form = Register()
    return render(request, 'index/register.html', {'register' : form})


def index(request):
    return render(request, 'index/index.html')


def instruction(request):
    return render(request, 'index/instruction.html')
