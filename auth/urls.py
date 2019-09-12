"""auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from homepage import views
from rendezvous_res import views as v

RvRouter = routers.DefaultRouter()
RvRouter.register('ff',v.Rv_View)

homepageRouter = routers.DefaultRouter()

homepageRouter.register('homepage', views.HomepageView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/v1/', include(homepageRouter.urls)),
    path('api/v1/',include(RvRouter.urls)),
    path('api/v1/', include("notification.urls")),
    path('api/v1/', include("student.urls")),
    path('api/v1/', include("notes.urls")),
    path('', include("booking.urls")),
    path('api/v1/', include("paiement.urls")),

    path('api/v1/', include("reclamation.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
