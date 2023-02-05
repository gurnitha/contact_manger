# apps/home/urls.py

# Import from django modules
from django.urls import path

# Import from locals
from apps.home import views

app_name='home'

urlpatterns = [
    path('', views.home, name='home'),
]