from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(
    models.User
)  # CustomUserAdmin 클래스의 아래부분에 admin.site.register(models.User,CustomUserAdmin) 을 작성한것과 같은기능을함
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    list_filter = UserAdmin.list_filter + ("superhost",)
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
    # list_display = ("username", "email", "gender", "language", "currency", "superhost")
    # list_filter = ("language", "currency", "superhost")