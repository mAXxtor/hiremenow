from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__reload__/', include('django_browser_reload.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('', include('hrsite.urls', namespace='hrsite')),
    path('internships/', include('internships.urls', namespace='internships')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
