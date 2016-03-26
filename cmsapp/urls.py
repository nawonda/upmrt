"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^blank/$', views.blank,name='blank'),
    url(r'^buttons/$', views.buttons,name='buttons'),
    url(r'^flot/$', views.flot,name='flot'),
    url(r'^forms/$', views.forms,name='forms'),
    url(r'^grid/$', views.grid,name='grid'),
    url(r'^icons/$', views.icons,name='icons'),
]
