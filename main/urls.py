from django.urls import path
from main.views import DestinationListView, HelpTemplateView

app_name = 'main'

urlpatterns = [
    path('', DestinationListView.as_view(), name='home'),
    path('help/', HelpTemplateView.as_view(), name='help')
]