from django.shortcuts import render
from index.form import Register

# Create your views here.


def log(request):
    login = Register()
    if request.method == 'POST':
        form1 = form.FormName(request.POST)
        if form1.is_valid():
            print("valid")
    context = {
        "login": login,
    }
    return render(request, 'index/login.html', context)


def index(request):
    return render(request, 'index/index.html')


def instruction(request):
    return render(request, 'index/instruction.html')
