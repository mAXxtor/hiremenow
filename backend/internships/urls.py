from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'internships'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('design/', views.DesignView.as_view(), name='design'),
    path('development/', views.DevView.as_view(), name='development'),
    path('management/', views.ManageView.as_view(), name='management'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
