from django.shortcuts import HttpResponse, render, redirect
from .models import Bug
from .forms import BugForm

# Create your views here.
def get_bugs_list(request):
    results = Bug.objects.all()
    return render(request, "bugs_list.html", {'bugs': results})
    
def create_a_new_bug(request):
    if request.method=="POST":
        new_bug = Bug()
        new_bug.title = request.POST.get('title')
        new_bug.ticket_status = request.POST.get('ticket_status')
        new_bug.description = request.POST.get('description')
        new_bug.save()
        
        return redirect(get_bugs_list)
    else:
        form = BugForm()
    return render(request, "create_a_bug.html", {'form': form})
    
def view_bug_details(request, pk):
    results = Bug.objects.find_one(pk)
    return render(request, "view_bug_detail.html", {'bugs': results})