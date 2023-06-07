from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

app_name = 'hrsite'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('internship/', include('internships.urls', namespace='internships')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
