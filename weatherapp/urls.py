from django.urls import path
from . import views
urlpatterns = [

    path('',views.home,name = 'home'),
    path('main',views.main,name = 'main'),
    path('weatherdata',views.weatherdata,name = 'weatherdata'),
    path('airdata',views.airdata,name = 'airdata'),
    path('contact',views.contact,name = 'contact')
]