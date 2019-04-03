"""python_proj7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from user_profile import views

# Todo: URL
#  make main URL and namespacing
#  should be Profile pg
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_profile/',
         include('user_profile.urls', namespace='user_profile')),
    path('', views.profile_detail, name='profile_detail')

    ]