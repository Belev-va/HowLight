from django.shortcuts import render

# Create your views here.
# pages/views.py
from django.views.generic import ListView, DetailView
 
from .models import Project
 
 
class PagesListView(ListView):
    model = Project
    template_name = 'home.html'

class PagesDetailView(DetailView):
    model = Project
    template_name = 'project.html'
    context_object_name = 'project'