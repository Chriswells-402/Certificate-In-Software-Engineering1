from django.urls import path
from . import views
#creating urls

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
]
    