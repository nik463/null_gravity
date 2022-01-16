from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('about-me/',about,name='about-me'),
    path('portfolio/',portfolio,name='portfolio'),
    path('projects/',projects,name='projects'),
    path("signup/", SignUp.as_view(), name="signup"),
]
