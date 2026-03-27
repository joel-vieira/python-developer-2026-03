from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "published_posts"

    def get_queryset(self) -> QuerySet:
        return Post.objects.order_by("-published_at")

class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"

def welcome(request: HttpRequest) -> HttpResponse:

    return render(request, "blog/welcome.html")
