# app/team/urls.py

# Import from django modules
from django.urls import path

# Import from locals
from app.team import views

app_name='team'

urlpatterns = [
    path('home/', views.teams_home, name='teams_home'),
    path('local/', views.teams_local, name='teams_local'),
    path('table/', views.teams_table, name='teams_table'),
    path('add/', views.teams_add, name='teams_add'),
]