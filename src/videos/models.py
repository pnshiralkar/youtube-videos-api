from django.db import models


# Create your models here.

class Video(models.Model):
    yt_id = models.CharField(max_length=20, unique=True)  # Video ID on YouTube
    published_at = models.DateTimeField()  # Timestamp of publish date-time
    title = models.TextField()
    description = models.TextField()
    thumbnail_url = models.TextField()  # URL for the thumbnail of medium size

    class Meta:
        # Database Indexes to make searching and order_by faster
        # Index on published_at: Used for sorting
        # Index on yt_id: Used for searching
        indexes = [
            models.Index(fields=['published_at']),
            models.Index(fields=['yt_id'])
        ]
