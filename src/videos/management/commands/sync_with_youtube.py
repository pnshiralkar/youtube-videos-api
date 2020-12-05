import datetime
import os
from time import sleep

from django.core.management.base import BaseCommand
from googleapiclient.discovery import build

from videos.models import Video

# Youtube API Config
DEVELOPER_KEY = os.environ['YOUTUBE_API_KEY']
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
SYNC_INTERVAL = int(
    os.environ['SYNC_INTERVAL'] if 'SYNC_INTERVAL' in os.environ else 10)


def youtube_search(query, max_results, published_after, page_token=None):
    """Search youtube for given query and return results"""

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=query,
        type='video',
        order='date',
        part='id,snippet',
        publishedAfter=published_after,
        pageToken=page_token,
        maxResults=max_results
    ).execute()
    return search_response


def save_new_videos(new_videos):
    """Save the new videos to database"""
    saved_count = 0
    for video in new_videos['items']:
        # Check if the video already exists in database
        # Prevents duplication of the latest video that repeats in the response
        video_check = Video.objects.filter(yt_id=video['id']['videoId'])
        if video_check.exists():
            continue

        # Video doesn't exist, so create save it
        Video.objects.create(
            yt_id=video['id']['videoId'],
            published_at=video['snippet']['publishedAt'],
            title=video['snippet']['title'],
            description=video['snippet']['description'],
            thumbnail_url=video['snippet']['thumbnails']['medium']['url']
        )
        saved_count += 1
    return saved_count


class Command(BaseCommand):
    """Django command to sync the DB with youtube API at specific interval"""

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write('Sync Service Started...')

        # Execute the code infinitely (executed at the interval defined)
        while True:
            # Get publish time of latest video IF there are videos in DB,
            # ELSE set it to 30 minutes before current time
            videos = Video.objects.all().order_by('-published_at')
            if videos.exists():
                published_after = videos.first().published_at.replace(
                    tzinfo=None)
            else:
                published_after = datetime.datetime.utcnow() - \
                                  datetime.timedelta(minutes=30)

            next_page = None
            published_after_str = published_after.isoformat("T") + "Z"
            saved_count = 0
            # Youtube API allows only 50 responses in one request,
            # so send multiple request with next page token
            while True:
                # Get new videos
                new_videos = youtube_search('football',
                                            50,
                                            published_after_str,
                                            next_page)
                # Save the videos to database
                num_videos = len(new_videos['items'])
                if num_videos > 0:
                    saved_count += save_new_videos(new_videos)

                # If response has next page token and number of videos in
                # current response is greater that 0, it means there are more
                # videos in further pages so set next_page  else break the loop
                if 'nextPageToken' in new_videos and num_videos > 0:
                    next_page = new_videos['nextPageToken']
                else:
                    break
            self.stdout.write(
                "Successfully synced at {} : Added {} new videos".format(
                    datetime.datetime.utcnow(),
                    saved_count
                ))

            # Sleep for the defined interval
            sleep(SYNC_INTERVAL)
