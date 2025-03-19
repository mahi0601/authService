from django.contrib import admin
from django.urls import path, include
from apps.common.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('apps.googleauth.urls')),
    path('drive/', include('apps.drive.urls')),
    path('chat/', include('apps.chat.urls')),
]
