from django.db import models
from django.contrib.auth.models import User


class Cantine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    meals = models.PositiveSmallIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.User.username)
