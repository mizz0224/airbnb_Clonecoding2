from django.contrib import admin
from . import models


@admin.register(
    models.User
)  # CustomUserAdmin 클래스의 아래부분에 admin.site.register(models.User,CustomUserAdmin) 을 작성한것과 같은기능을함
class CustomUserAdmin(admin.ModelAdmin):
    pass

    """ Custom User Admin """

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")