from django.contrib import admin

# Register your models here.
from videos.models import Video


class VideoAdmin(admin.ModelAdmin):
    # list_filter = ('title', 'yt_id')
    sortable_by = ('published_at',)
    list_display = ('yt_id', 'title', 'published_at')


admin.site.register(Video, VideoAdmin)
