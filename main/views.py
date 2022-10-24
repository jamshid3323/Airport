from django.shortcuts import render
from django.views.generic import TemplateView
from .models import RecommendationDestinationsModel
from django.views.generic import ListView
from .models import RecommendationDestinationsModel, DiscoverModel


class DestinationListView(ListView):
    template_name = 'base.html'

    def get_queryset(self):
        return RecommendationDestinationsModel.objects.filter()[:4]

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['discover'] = DiscoverModel.objects.filter()[:3]
        return data
