# pages/urls.py
from django.urls import path
from .views import PagesListView, PagesDetailView
 
urlpatterns = [
    path('', PagesListView.as_view(), name='home'),
    path('<int:pk>', PagesDetailView.as_view(), name='project-detail'),
]