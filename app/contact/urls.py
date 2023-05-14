# app/contact/urls.py

# Import from django modules
from django.urls import path

# Import from locals
from app.contact import views

app_name='contact'

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('list/', views.contacts_list, name='contacts_list'),
    path('profile/', views.contact_profile, name='contact_profile'),
    path('add-contact/', views.add_contact, name='add_contact'),
]