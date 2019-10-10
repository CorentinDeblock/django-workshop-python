from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)


