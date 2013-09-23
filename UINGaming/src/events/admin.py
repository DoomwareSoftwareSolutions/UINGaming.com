from django.contrib import admin
from src.events.models import Event,EventMembership

admin.site.register(Event)
admin.site.register(EventMembership)
