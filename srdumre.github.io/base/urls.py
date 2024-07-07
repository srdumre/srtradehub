from django.urls import path
from .views import inquiry_view,home
from . import  views
urlpatterns = [
    
    path('', home, name='home'),
    path('inquiry/', inquiry_view, name='inquiry'),
]

