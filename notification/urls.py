from django.urls import path,include
from . import views
from rest_framework import routers

notifRouter=routers.DefaultRouter()
notifRouter.register('notification',views.NotifView)
urlpatterns = [

    path('',include(notifRouter.urls))
]