"""
URL configuration for blog pages.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("posts/", views.index, name="index"),
    path("", views.welcome, name="welcome"),
]
