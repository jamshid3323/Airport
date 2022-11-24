from django.shortcuts import render, reverse
from django.views.generic import TemplateView
from main.models import RecommendationDestinationsModel, CityModel
from django.views.generic import ListView, TemplateView, CreateView, DetailView
from main.models import RecommendationDestinationsModel, DiscoverModel, CheapFlightModel
from .forms import MessageModelForm
from .models import MessageModel, FlightModel
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER
from .utils import send_bot_message


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
        data = super().get_context_data(**kwargs)
        data['discover'] = DiscoverModel.objects.filter()[:3]
        data['cheap'] = CheapFlightModel.objects.filter()[:4]
        data['flight'] = FlightModel.objects.all()
        data['city'] = CityModel.objects.all()
        s = self.request.GET.get('status')
        if s:
            data['status'] = s
            data['detail'] = FlightModel.objects.get(series=s)
        return data


class MessageView(CreateView):
    model = MessageModel
    form_class = MessageModelForm
    template_name = 'layouts/help.html'

    def get_success_url(self):
        return reverse("main:message")

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        # message = f"Assalomu alaykum {form.instance.email} foydalanuvchisi ! Xabaringiz qabul qilindi."
        # send_mail('Xayrli kun', message, EMAIL_HOST_USER, [form.instance.email])
        send_bot_message(form.cleaned_data)
        return super().form_valid(form)
