from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    is_done = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
