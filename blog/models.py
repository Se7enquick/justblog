from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    post_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('blog.Tag')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=36)

    def __str__(self):
        return self.name
