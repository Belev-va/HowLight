# pages/urls.py
from django.urls import path
from .views import PagesListView
 
urlpatterns = [
    path('', PagesListView.as_view(), name='home')
]