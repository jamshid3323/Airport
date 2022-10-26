from django.shortcuts import render
from django.views.generic import TemplateView
from .models import RecommendationDestinationsModel
from django.views.generic import ListView
from .models import RecommendationDestinationsModel, DiscoverModel, CheapFlightModel


class DestinationListView(ListView):
    template_name = 'base.html'

    def get_queryset(self):
        qs = RecommendationDestinationsModel.objects.filter()[:4]
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['discover'] = DiscoverModel.objects.filter()[:3]
        data['cheap'] = CheapFlightModel.objects.filter()[:4]
        return data
