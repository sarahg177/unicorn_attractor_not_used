from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from .models import Bug, Comments
from .forms import BugForm, CommentForm
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
    
def view_bug_details(request, pk):
    """Create a view that will return a single ticket object based on the ticket ID(pk) and render it to the 'view_bug_details.html' template. Or return a 404 error if the post is not found"""
    bug = get_object_or_404(Bug, pk=pk)
    bug.views +=1
    bug.save()
    return render(request, "view_bug_detail.html", {'bug': bug})

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