from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name = 'welcome'),
    path('AboutUs', views.AboutUs, name = 'AboutUs'),
    path('ContactUs', views.ContactUs, name = 'ContactUs'),
    path('places', views.places, name = 'places'),
]