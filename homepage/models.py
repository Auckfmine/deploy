from django.db import models


class Homepage(models.Model):
    group_choices = (('petit-section', 'Petit-Section'), ('moyenne-section', 'Moyenne-Section'), ('grand-section', 'Grand-Section'))
    theme = models.CharField(max_length=100)
    Planning = models.ImageField(upload_to="planning/")
    message = models.TextField(default=' ', null=True)
    daily_img = models.ImageField(upload_to="daily-img/", null=True)
    group = models.CharField(max_length=250, choices=group_choices)
    Event_title = models.CharField(blank=True,max_length=100)
    Event_description = models.TextField(null=True,blank=True,default=' ')
    Event_date = models.DateField(blank=True,null=True   )
    Event_img = models.ImageField(upload_to="events/", null=True)


'''class Events(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default=' ')
    date = models.DateField()
    img = models.ImageField(upload_to="events/", null=True)
    #group= models.ForeignKey(Enfant,on_delete=models.CASCADE)
'''
