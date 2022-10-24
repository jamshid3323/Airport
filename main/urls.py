from django.urls import path
from .views import DestinationListView

app_name = 'main'

urlpatterns = [
    path('', DestinationListView.as_view(), name='home'),
]