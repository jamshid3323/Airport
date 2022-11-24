from django.contrib import admin
from .models import *


@admin.register(SeatModel)
class SeatModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'name']
    list_display_links = ['id', 'number']


@admin.register(TicketModel)
class TicketModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'flight', 'price', 'seat']
    list_display_links = ['id', 'flight']
