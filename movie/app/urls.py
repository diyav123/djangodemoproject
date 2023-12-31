"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app import views

app_name="app"
urlpatterns=[
    path('',views.view,name="view"),
    path('add/',views.add,name="add"),
    path('add1/',views.add1,name="add1"),
    path('view1/<int:p>', views.view1, name="view1"),
    path('deleteby1/<p>', views.deleteby1, name="deleteby1"),
    path('editby1/int:<p>',views.editby1,name="editby1"),
]
