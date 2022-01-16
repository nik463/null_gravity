from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from django.template import loader
from django.http import HttpResponse

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



def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:
        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))
