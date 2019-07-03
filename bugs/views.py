from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from .models import Bug, Comments
from .forms import BugForm, CommentForm
from django.contrib.auth.decorators import login_required


def get_bugs_list(request):
    """Shows list of all bugs"""
    results = Bug.objects.all()
    return render(request, "bugs_list.html", {'bugs': results})

@login_required    
def create_a_new_bug(request):
    """View to allow new ticket to be added"""
    if request.method=="POST":
        form = BugForm(request.POST, request.FILES)
        if form.is_valid():
            form.username = request.user
            form.save()
            return redirect('get_bugs_list')
    else:
        form = BugForm()
    return render(request, "create_a_bug.html", {'form': form})
    
def view_bug_details(request, pk):
    """Create a view that will return a single ticket object based on the ticket ID(pk) and render it to the 'view_bug_details.html' template showing comments made. Or return a 404 error if the post is not found"""
    bug = get_object_or_404(Bug, pk=pk)
    bug.views +=1
    bug.save()
    form = CommentForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('view_bug_details')
    else:
        form = CommentForm()
    return render(request, "view_bug_detail.html", {'bug': bug}, {'form': form})

@login_required
def edit_a_bug(request, id):
    """Edit a ticket"""
    bug = get_object_or_404(Bug, pk=id)
    if request.method=="POST":
        form = BugForm(request.POST, instance = bug)
        if form.is_valid():
            form.save()
            return redirect(get_bugs_list)
    else:
        form = BugForm(instance=bug)
    return render(request, "create_a_bug.html", {'form': form})
    
@login_required
def add_comment(request, pk=None):
    """Add comments to tickets"""
    bug = get_object_or_404(Bug, pk=pk)
    form = CommentForm(request.POST, request.FILES)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.username = request.user
        instance.bug = bug
        form.save()
        return redirect(view_bug_details, bug.pk)
        
    return render(request, "create_a_new_bug.html", {'form': form})