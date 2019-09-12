from django.contrib import admin

from django.contrib import admin
from .models import Homepage


class Homepage_admin(admin.ModelAdmin):

    list_display=['group','theme']
    search_fields=['group']




admin.site.register(Homepage,Homepage_admin)
