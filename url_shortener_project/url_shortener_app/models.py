# url_shortener_app/models.py
from django.db import models
import shortuuid

class URL(models.Model):
    original_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=10, unique=True)
    short_code = models.CharField(max_length=22, default=shortuuid.uuid, unique=True)


