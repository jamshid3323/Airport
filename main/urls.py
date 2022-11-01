from django.urls import path
from main.views import DestinationListView, HelpTemplateView, LoginTemplateView, SignUpTemplateView

app_name = 'main'

urlpatterns = [
    path('', DestinationListView.as_view(), name='home'),
    path('help/', HelpTemplateView.as_view(), name='help'),
    path('login/', LoginTemplateView.as_view(), name='login'),
    path('signup/', SignUpTemplateView.as_view(), name='signup')
]