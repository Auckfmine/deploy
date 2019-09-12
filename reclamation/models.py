from django.db import models
from django.contrib.auth.models import User

class reclamation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    title = models.CharField(blank=True, max_length=100)
    msg = models.CharField(null=True,blank=True, max_length=100)
    def __str__(self):
        return str(self.user.username)