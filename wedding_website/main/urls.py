from django.urls import path
from .views import rsvp_view  # Ensure you're importing the view, not a model
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rsvp/', rsvp_view, name='rsvp'),
]
