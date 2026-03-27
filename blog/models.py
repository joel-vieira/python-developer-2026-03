import uuid

from django.db import models  # noqa: F401


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField("Full Name", max_length=200)
    created_at = models.DateTimeField("Created At")
    modified_at = models.DateTimeField("Last Modified At")


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=100)
    body = models.TextField("Body")
    created_at = models.DateTimeField("Created At")
    modified_at = models.DateTimeField("Last Modified At")
    published_at = models.DateTimeField("Published At")
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="posts", verbose_name="Author"
    )
