# scheduler_app/urls.py

# scheduler_app/urls.py
"""
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]""" 

from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]


