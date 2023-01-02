from django.shortcuts import render

# Create your views here.
# pages/views.py
from django.views.generic import ListView
 
from .models import Project
 
 
class PagesListView(ListView):
    model = Project
    template_name = 'home.html'