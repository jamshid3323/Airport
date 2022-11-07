from django.shortcuts import render, reverse
from django.views.generic import TemplateView
from main.models import RecommendationDestinationsModel
from django.views.generic import ListView, TemplateView, CreateView
from main.models import RecommendationDestinationsModel, DiscoverModel, CheapFlightModel
from .forms import MessageModelForm
from .models import MessageModel

class SignUpTemplateView(TemplateView):
    template_name = 'layouts/signup.html'


class LoginTemplateView(TemplateView):
    template_name = 'layouts/login.html'


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


class MessageView(CreateView):
    model = MessageModel
    form_class = MessageModelForm
    template_name = 'layouts/help.html'

    def get_success_url(self):
        return reverse("main:message")
