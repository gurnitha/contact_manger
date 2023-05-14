# apps/task/views.py

# Import from django modules
from django.shortcuts import render

# Import from loclas


# TASK_LIST
def tasks_list(request):
	return render(request, 'app/task/tasks_list.html')