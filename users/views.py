from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import RegisterForm, UserRegistrationForm, LoginForm

def index(request):
    return render(request, 'users/index.html')

def register(request):
    use_custom = True
    if request.method == 'POST':
        if use_custom:
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                return render(request, 'users/register_done.html')
            else:
                user_form = UserRegistrationForm()
            return render(request, 'users/register.html', {'user_form': user_form})
        else:
            form = RegisterForm(request.POST)
            if form.is_valid(): # checked unique user id
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Welcome {username}, your account is created!')
            return render(request, 'users/index.html')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponse("user authenticated and logged in")
            else:
                return HttpResponse("Invalid credentials")
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

def register_done(request):
    return render(request, 'portfolio/index.html')