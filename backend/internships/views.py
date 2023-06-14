from typing import Any
from django.db.models.query import QuerySet
from django.views.generic.list import ListView

from .models import Internship


class InternshipListView(ListView):
    """ Список опубликованных стажировок. """
    model = Internship
    template_name = 'internships/index.html'
    context_object_name = 'internships'

    def get_queryset(self) -> QuerySet[Any]:
        return Internship.objects.prefetch_related('fields').filter(
            visibility=True)


class FieldListView(InternshipListView):
    """ Список опубликованных стажировок по направлению. """
    allow_empty = False

    def get_queryset(self) -> QuerySet[Any]:
        return Internship.objects.prefetch_related('fields').filter(
            fields__slug=self.kwargs['slug'], visibility=True)
