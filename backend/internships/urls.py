from django.urls import path

from . import views

app_name = 'internships'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('design/', views.DesignView.as_view(), name='design'),
    path('development/', views.DevView.as_view(), name='development'),
    path('management/', views.ManageView.as_view(), name='management'),
]
