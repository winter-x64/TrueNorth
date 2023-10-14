from django.shortcuts import render


# Create your views here.
def user_dashboard(request):
    return render("homepage/user_dashboard.html")
