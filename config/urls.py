# config/urls.py

# Import from django modules
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Import from locals

urlpatterns = [

    # home
    path('', include('app.home.urls', namespace='home')),
    
    # contact
    path('contacts/', include('app.contact.urls', namespace='contact')),

    # team
    path('teams/', include('app.team.urls', namespace='team')),

    # task
    path('tasks/', include('app.task.urls', namespace='task')),

    # admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)