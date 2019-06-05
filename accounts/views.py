from django.shortcuts import render
from accounts.forms import UserLoginForm

# Create your views here.
def login(request):
    """Return a login page"""
    login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})