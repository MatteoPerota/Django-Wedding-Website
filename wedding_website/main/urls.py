from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rsvp/', views.rsvp, name='rsvp'),
]