from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from . import api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    path('pusher_auth/', api.pusher_auth)
]
