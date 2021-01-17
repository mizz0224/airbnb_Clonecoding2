# from django.shortcuts import render, redirect
# from django.core.paginator import EmptyPage, Paginator
# from . import models


# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     try:
#         rooms = paginator.page(int(page))
#         return render(request, "rooms/home.html", {"page": rooms})
#     except EmptyPage:
#         return redirect("/")
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries

# from django.urls import reverse
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


# https://ccbv.co.uk/projects/Django/2.2/
# from django.http import Http404
# from django.shortcuts import redirect, render
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         # return redirect(reverse("core:home"))
#         raise Http404()


class RoomDetail(DetailView):
    """ RoomDeail Definition """

    model = models.Room
    # urls.py  int:pk  pk -> potato ,  RoomDetail class pk_url_kwarg = "potato"
    # https://ccbv.co.uk/projects/Django/2.2/


def search(request):
    city = request.GET.get("city", "")
    city = str.capitalize(city)
    room_types = models.RoomType.objects.all()
    return render(
        request,
        "rooms/search.html",
        {"city": city, "countries": countries, "room_types": room_types},
    )
