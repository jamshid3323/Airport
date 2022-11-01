from django.urls import path
from main.views import DestinationListView, HelpTemplateView, LoginTemplateView

app_name = 'main'

urlpatterns = [
    path('', DestinationListView.as_view(), name='home'),
    path('help/', HelpTemplateView.as_view(), name='help'),
    path('login/', LoginTemplateView.as_view(), name='login')
]