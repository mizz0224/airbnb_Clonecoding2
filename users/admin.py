from django.contrib import admin
from . import models


@admin.register(
    models.User
)  # CustomUserAdmin Ŭ������ �Ʒ��κп� admin.site.register(models.User,CustomUserAdmin) �� �ۼ��ѰͰ� �����������
class CustomUserAdmin(admin.ModelAdmin):
    pass

    """ Custom User Admin """

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")