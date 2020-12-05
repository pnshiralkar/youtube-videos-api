# Create your views here.
from django.core.paginator import Paginator, EmptyPage
from django.forms import model_to_dict
from django.http import JsonResponse

from videos.models import Video


def get_videos(request):
    videos = Video.objects.all().order_by('-published_at')
    paginator = Paginator(videos, 50)
    page_no = int(request.GET.get('page') or '1')
    try:
        paginated_videos = paginator.page(page_no)
    except EmptyPage:
        return JsonResponse({"details": "Page out of range"}, status=404)
    next_page = paginated_videos.next_page_number() \
        if paginated_videos.has_next() else None
    prev_page = paginated_videos.previous_page_number() \
        if paginated_videos.has_previous() else None
    return JsonResponse({
        "next_page": next_page,
        "previous_page": prev_page,
        "videos": [model_to_dict(v) for v in list(paginated_videos)]
    })
