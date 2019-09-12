from django.contrib import admin

from .models import Notif


class RvAdmin(admin.ModelAdmin):
    list_filter = ['date']
    list_display = ['titre', 'date']
    search_fields = ['titre']

admin.site.register(Notif,RvAdmin)