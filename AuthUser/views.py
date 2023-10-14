from django.shortcuts import HttpResponse, render


def login_view(request):
    return render(request, "login/auth_login.html")


def logout_view(request):
    return HttpResponse("Logged out")


def signup_view(request):
    return render(request, "register/auth_signup.html")


def register(request):
    return render(request, "")


def lets_me_in(request):
    return render(request, "")
