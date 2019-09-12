from django.urls import include, path

urlpatterns = [

    path('accounts/', include('rest_auth.urls')),
    path('accounts/registration/', include('rest_auth.registration.urls')),
]
