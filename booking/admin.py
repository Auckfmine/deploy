from django.contrib import admin
from .models import Cantine


class RvAdmin(admin.ModelAdmin):
    list_filter = ['date']
    list_display = ['user', 'date','meals']
    search_fields = ['user']


# admin.site.register(RvAdmin)
admin.site.register(Cantine, RvAdmin)
