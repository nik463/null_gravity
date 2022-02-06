from django.shortcuts import render
from coviddash.dashitems import coviddash

# Create your views here.

def covid(request):
    return render(request,'covid.html')