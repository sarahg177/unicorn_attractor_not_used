from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from .models import Bug
from .forms import BugForm
from django.contrib.auth.decorators import login_required

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
    
def view_bug_details(request, id):
    results = Bug.objects.find_one(Bug, pk=id)
    return render(request, "view_bug_detail.html", {'bugs': results})

def edit_a_bug(request, id):
    bug = get_object_or_404(Bug, pk=id)
    if request.method=="POST":
        form = BugForm(request.POST, instance = bug)
        if form.is_valid():
            form.save()
            return redirect(get_bugs_list)
    else:
        form = BugForm(instance=bug)
    return render(request, "create_a_bug.html", {'form': form})