from django.shortcuts import render
from django.views.generic import TemplateView
from main.models import RecommendationDestinationsModel
from django.views.generic import ListView, TemplateView
from main.models import RecommendationDestinationsModel, DiscoverModel, CheapFlightModel


class HelpTemplateView(TemplateView):
    template_name = 'layouts/help.html'


class DestinationListView(ListView):
    template_name = 'layouts/home.html'

    def get_queryset(self):
        qs = RecommendationDestinationsModel.objects.filter()[:4]
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data()
        data['discover'] = DiscoverModel.objects.filter()[:3]
        data['cheap'] = CheapFlightModel.objects.filter()[:4]
        return data
