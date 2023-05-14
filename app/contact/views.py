# app/contact/views.py

# Import from django modules
from django.shortcuts import render

# Import from loclas


# CONTACT_LIST
def contacts(request):
	return render(request, 'app/contact/contacts.html')


# CONTACT_LIST_3
def contacts_list(request):
	return render(request, 'app/contact/contacts_list.html')


# CONTACT_LIST_3
def add_contact(request):
	return render(request, 'app/contact/add_contact.html')


# CONTACT_PROFILE
def contact_profile(request):
	return render(request, 'app/contact/contact_profile.html')