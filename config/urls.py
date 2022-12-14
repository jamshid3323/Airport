from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path('client/', include('client.urls')),
    path('', include('main.urls')),
    path('tickets/', include('tickets.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
