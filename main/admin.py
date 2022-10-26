from django.contrib import admin
from .models import RecommendationDestinationsModel, DiscoverModel, CheapFlightModel


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