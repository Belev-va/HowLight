from django.shortcuts import render, redirect

# Create your views here.
# news/views.py
from django.views.generic import DetailView, ListView
 
from .models import Article
 

class NewsListView(ListView):
    model = Article
    template_name = 'news.html'

class NewsDetailView(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'