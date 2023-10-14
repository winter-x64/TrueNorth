from django.urls import path

from . import views

urlpatterns = [
    # View patterns
    path("login/", views.login_view),
    path("logout/", views.logout_view),
    path("signup/", views.signup_view),
    # post patterns
    path("login_me/", views.lets_me_in),
    path("register/", views.register),
]
