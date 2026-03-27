"""
URL configuration for blog pages.
"""

from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("posts/", views.IndexView.as_view(), name="index"),
    path("posts/<uuid:pk>", views.DetailView.as_view(), name="detail"),
    path("", views.welcome, name="welcome"),
]
