from django.urls import path, include

app_name = 'client'

urlpatterns = [
    path('', include('django.contrib.auth.urls'))
]