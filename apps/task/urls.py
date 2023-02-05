# apps/task/urls.py

# Import from django modules
from django.urls import path

# Import from locals
from apps.task import views

app_name='task'

urlpatterns = [
    path('', views.tasks_list, name='tasks_list'),
]