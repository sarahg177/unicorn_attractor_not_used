from django.shortcuts import render
from .models import Feature

# Create your views here.
def get_features_list(request):
    results = Feature.objects.all()
    return render(request, "features_list.html", {'features': results})