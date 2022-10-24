from django.shortcuts import render
from django.views.generic import TemplateView
from .models import RecommendationDestinationsModel
from django.views.generic import ListView
from .models import RecommendationDestinationsModel


class TestView(TemplateView):
    template_name = 'base.html'


class DestinationListView(ListView):
    queryset = RecommendationDestinationsModel.objects.filter()[:4]
    template_name = 'base.html'
