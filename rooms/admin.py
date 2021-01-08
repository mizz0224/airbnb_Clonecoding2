from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


class PhotoInline(admin.TabularInline):
    # TabularInline 은 한줄에 여러개(caption, file, delete), StackedInline 은 한개당 한줄(cpation 한줄, file 한줄, delete 한줄)
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    inlines = (PhotoInline,)
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
        "fake_rooms",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
        "fake_rooms",
    )
    raw_id_fields = ("host",)
    search_fields = (
        "=city",
        "^host__username",
    )  # xaaa : x가 ^ <- aaa로 시작 , = <- aaa와 완전히일치(대소문자 구별x), @ <- aaa , none(아무것도 없음) <- icontatins(포함)
    filter_horizontal = ("amenities", "facilities", "house_rules")
    # fields = "country" : admin에서  country만 표시
    # def save_model(self, request, obj, form, change):               <- model의 save와 달리 이건 admin에서만 작동

    #     super().save_model(self, request, obj, form, change)

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Phot Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"