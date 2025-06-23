from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login


def register_view(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request,'registration.html', context={'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')

    else:
        form = LoginForm()

    return render(request, 'login.html', context={'form': form})