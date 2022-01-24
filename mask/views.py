from django.shortcuts import render
from mask.dashitems import mask

# Create your views here.

def mask(request):
    return render(request,'mask.html')