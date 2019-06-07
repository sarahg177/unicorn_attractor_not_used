from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render (request, "index.html")
 
@login_required   
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('home'))