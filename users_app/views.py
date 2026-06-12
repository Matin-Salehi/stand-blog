from django.shortcuts import render


def login(request):
    return render(request, "users_app/login.html", {})