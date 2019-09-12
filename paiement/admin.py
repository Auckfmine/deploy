from django.contrib import admin
from .models import paiement
from django.db import connection
import datetime

class paiement_db(admin.ModelAdmin):
    list_display=['user','paye','date','valid_until']
    search_fields=['user__username']
    """def upadate(self,request,*args,**kwargs):
        a=paiement.objects.all()
        for i in a :
            if  datetime.date.today() == self.valid_until:
                i.paye=False
                i.save()"""






admin.site.register(paiement,paiement_db)
