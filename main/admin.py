from django.contrib import admin
from .models import *


@admin.register(DiscoverModel)
class DiscoverModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


@admin.register(RecommendationDestinationsModel)
class RecommendationDestinationsAdmin(admin.ModelAdmin):
    list_display = ['id', 'where_to']
    list_display_links = ['id', 'where_to']


@admin.register(CheapFlightModel)
class CheapFlightModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'where_to']
    list_display_links = ['id', 'where_to']


@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']
    list_display_links = ['id', 'email']


@admin.register(AirCompanyModel)
class AirCompanyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']