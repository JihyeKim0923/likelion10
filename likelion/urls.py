from django.contrib import admin
from django.urls import path, include
import festival,accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('festival/',include('festival.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]
