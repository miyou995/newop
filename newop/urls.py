
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from newop import settings
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("opapp.urls")),
]

# urlpatterns += i18n_patterns()


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
