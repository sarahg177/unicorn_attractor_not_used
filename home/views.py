from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.
def home(request):
    return render (request, "index.html")
    
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('home'))