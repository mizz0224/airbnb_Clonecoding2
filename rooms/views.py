from django.shortcuts import render
from . import models
from math import ceil


def all_rooms(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = models.Room.objects.count() / page_size
    ceil_page_count = ceil(page_count)
    return render(
        request,
        "rooms/home.html",
        context={
            "potato": all_rooms,
            "page": page,
            "page_count": ceil_page_count,
            "page_range": range(1, ceil_page_count + 1),
        },
    )
