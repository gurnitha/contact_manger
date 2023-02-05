# apps/home/views.py

# Import from django modules
from django.shortcuts import render

# Import from loclas


# HOME
def home(request):
	return render(request, 'apps/home/home.html')
