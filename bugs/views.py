from django.shortcuts import HttpResponse, render, redirect
from .models import Bug
from .forms import BugForm

# Create your views here.
def get_bugs_list(request):
    results = Bug.objects.all()
    return render(request, "bugs_list.html", {'bugs': results})
    
def create_a_new_bug(request):
    if request.method=="POST":
        form = BugForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_bugs_list)
    else:
        form = BugForm()
    return render(request, "create_a_bug.html", {'form': form})