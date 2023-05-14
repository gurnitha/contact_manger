# app/team/views.py

# Import from django modules
from django.shortcuts import render

# Import from loclas


# TEAMS_HOME
def teams_home(request):
	return render(request, 'app/team/teams_home.html')


# TEAMS_LOCAL
def teams_local(request):
	return render(request, 'app/team/teams_local.html')


# TEAMS_TABLE
def teams_table(request):
	return render(request, 'app/team/teams_table.html')


# TEAMS_ADD
def teams_add(request):
	return render(request, 'app/team/teams_add.html')