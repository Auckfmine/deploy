from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils import timezone


def next_month():
    month = date.today().month+1
    year = date.today().year
    day = 1
    return date(year, month, day)

class paiement(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    paye=models.BooleanField(default=False)
    date = models.DateTimeField(verbose_name='date',auto_now_add=True)
    valid_until= models.DateField(verbose_name='valid until',default=next_month())

    def __str__(self):
        return self.user.username

    """def notif_date(self):
        month= self.valid_until.month
        year=self.valid_until.year
        day=self.valid_until.day+5
        return date(year,month,day)

    def notif(self):
        if datetime.date.today()==self.notif_date:
            if self.paye==False:
                print('send notif')"""
