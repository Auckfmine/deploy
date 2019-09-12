from django.db import models

class Notif(models.Model):
    titre = models.CharField(max_length=120,null=True)
    corp_de_la_notification = models.CharField(max_length=250,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.titre