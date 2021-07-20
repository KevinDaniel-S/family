from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.family, name='family'),
    path('family/', include([
        path('', views.family, name='family'),
    ])),
]
