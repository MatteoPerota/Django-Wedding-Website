from django.contrib import admin
from .models import RSVP

@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'attending')
