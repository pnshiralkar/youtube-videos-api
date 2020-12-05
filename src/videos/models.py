from django.db import models


# Create your models here.

class Video(models.Model):
    yt_id = models.CharField(max_length=20, unique=True)
    published_at = models.DateTimeField()
    title = models.TextField()
    description = models.TextField()
    thumbnail_url = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['published_at']),
            models.Index(fields=['yt_id'])
        ]

