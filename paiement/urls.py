from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('paiement',views.PaiementView,base_name='paiement')
urlpatterns = [

    path('',include(router.urls))
]
