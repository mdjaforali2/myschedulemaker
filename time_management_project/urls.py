# urls.py in time_management_project

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('time_management_app.urls')),
]
