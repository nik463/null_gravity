from django.urls import path,re_path
from .views import *

from portfolio import views

urlpatterns = [
    path('',home,name='home'),
    path('about-me/',about,name='about-me'),
    path('portfolio/',portfolio,name='portfolio'),
    path('projects/',projects,name='projects'),
    path("signup/", SignUp.as_view(), name="signup"),
]

# urlpatterns = [
#     # Matches any html file - to be used for gentella
#     # Avoid using your .html in your resources.
#     # Or create a separate django app.
#     re_path(r'^.*\.html', views.pages, name='pages'),

#     # The home page
#     path('', views.index, name='home'),
# ]
