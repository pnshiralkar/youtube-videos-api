"""videos app URL Configuration"""

from django.urls import path

from videos.views import get_videos

urlpatterns = [
    path('', get_videos)
]
