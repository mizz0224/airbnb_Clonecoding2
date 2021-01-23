from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(
    models.User
)  # CustomUserAdmin Ŭ������ �Ʒ��κп� admin.site.register(models.User,CustomUserAdmin) �� �ۼ��ѰͰ� �����������
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
                    "login_method",
                )
            },
        ),
    )
    list_filter = UserAdmin.list_filter + ("superhost", "fake_users")
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
        "fake_users",
        "email_verified",
        "email_secrete",
        "login_method",
    )
    # list_display = ("username", "email", "gender", "language", "currency", "superhost")
    # list_filter = ("language", "currency", "superhost")