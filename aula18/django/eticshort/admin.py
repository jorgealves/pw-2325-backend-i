from django.contrib import admin

from django.eticshort.models import UrlShort


@admin.register(UrlShort)
class UrlAdmin(admin.ModelAdmin):
    pass


