"""
URL configuration for blog pages.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("posts/", views.IndexView.as_view(), name="index"),
    path("", views.welcome, name="welcome"),
]
