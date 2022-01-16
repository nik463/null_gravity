from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
    return render(request,'index.html')
    
def about(request):
    return render(request,'about.html')

def portfolio(request):
    return render(request,'portfolio.html')

def projects(request):
    return render(request,'project.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
