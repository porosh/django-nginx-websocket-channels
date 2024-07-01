"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from websocket_app import routing as websocket_routing
from websocket_app.views import test_websocket_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_websocket/', test_websocket_view),  # Add this line
]

# Include websocket URL routing
websocket_urlpatterns = websocket_routing.websocket_urlpatterns
