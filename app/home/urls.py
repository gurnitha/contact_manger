# app/home/urls.py

# Import from django modules
from django.urls import path

# Import from locals
from app.home import views

app_name='home'

urlpatterns = [
    path('', views.home, name='home'),
]