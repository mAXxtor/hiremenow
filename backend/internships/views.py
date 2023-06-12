from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView

from .models import Internship, InternshipField


class IndexView(TemplateView):
    template_name = 'internships/index.html'


def index(request):
    internships = Internship.objects.prefetch_related('fields').all()
    return render(request, 'internships/index.html',
                  context={'internships': internships})


class DesignView(TemplateView):
    template_name = 'internships/index.html'


class DevView(TemplateView):
    template_name = 'internships/index.html'


class ManageView(TemplateView):
    template_name = 'internships/index.html'
