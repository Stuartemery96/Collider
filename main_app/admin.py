from django.contrib import admin
from .models import Event, Collide, Rsvp, Rating


# Register your models here.
admin.site.register(Event)
admin.site.register(Collide)
admin.site.register(Rsvp)
admin.site.register(Rating)