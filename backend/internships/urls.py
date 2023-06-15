from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'internships'

urlpatterns = [
    path('', views.InternshipListView.as_view(), name='index'),
    path('<slug:slug>/', views.InternshipFieldListView.as_view(),
         name='internship_field_list'),
    path()
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
