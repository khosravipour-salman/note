from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from app.forms import LoginForm


@login_required()
def index(request):
    return render(request, 'app/index.html')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'app/register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd.get('username'), password=cd.get('password'))

            if user:
                login(request, user=user)
                return redirect('index')

    form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'app/login.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')
