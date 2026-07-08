from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    else:
        if request.method == "POST":
            form = LoginForm(
                request=request,
                data=request.POST or None,
            )
            if form.is_valid():
                login(request, form.get_user())

                return redirect('home_app:home')

            else:
                pass
        else:
            form = LoginForm()
    return render(request, "users_app/login.html", {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home_app:home')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('pass1')
            password2 = request.POST.get('pass2')
            errors = []
            if User.objects.filter(username=username).exists():
                errors.append("Username already exists")

            if User.objects.filter(email=email).exists():
                errors.append("Email already exists")

            if password1 != password2:
                errors.append("Passwords do not match")

            if errors:
                return render(request, "users_app/register.html", {
                    "errors": errors,
                    "username": username,
                    "email": email,
                })

            User.objects.create_user(
                username=username,
                email=email,
                password=password1,
            )
            return redirect('users_app:login')
    return render(request, "users_app/register.html", {})
