from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    summary = models.TextField(null=True)
    body = models.TextField()
    image_name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments', null=True)
    author = models.CharField(max_length=200, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
