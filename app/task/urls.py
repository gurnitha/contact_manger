# app/task/urls.py

# Import from django modules
from django.urls import path

# Import from locals
from app.task import views

app_name='task'

urlpatterns = [
    path('', views.tasks_list, name='tasks_list'),
]