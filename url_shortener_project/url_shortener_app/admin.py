#from django.contrib import admin

# Register your models here.
# url_shortener_app/admin.py
from django.contrib import admin
from .models import URL

admin.site.register(URL)