from django.shortcuts import render
from coviddash.dashitems import SimpleExample

# Create your views here.

def covid(request):
    return render(request,'covid.html')