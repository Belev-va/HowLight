from django.shortcuts import render

# Create your views here.
# pages/views.py
from django.views.generic import ListView
 
from .models import Post
 
 
class PagesListView(ListView):
    model = Post
    template_name = 'home.html'