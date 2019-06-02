from django.shortcuts import render
from .models import Bug

# Create your views here.
def get_bugs_list(request):
    results = Bug.objects.all()
    return render(request, "bugs_list.html", {'bugs': results})