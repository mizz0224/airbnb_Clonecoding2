from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:  # <-이거 하는 이유 : 데이터베이스에 등록되지 않게 하기 위해서
        abstract = True