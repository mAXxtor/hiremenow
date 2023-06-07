from django.contrib import admin

from .models import Internship, InternshipField


# class InternshipFieldInline(admin.TabularInline):
#     model = InternshipsFields
#     min_num = 1


@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    """ Управление Стажировками """
    fields = ('name', 'short_description', 'start_date', 'end_date',
              'is_permanent', 'fields', 'visibility', )
    search_fields = ('name',)
    list_filter = ('name', 'visibility')
    list_display = ('name', 'fields',)
    # list_editable = ('visibility', 'is_permanent',)
    # fieldsets = ('get_internships_fields',)
    # inlines = (InternshipFieldInline,)

    # def get_internships_fields(self, internship):
    #     return [field.name for field in internship.fields.all()]



@admin.register(InternshipField)
class InternshipFieldAdmin(admin.ModelAdmin):
    """ Управление направлением стажировок """
    fields = ('name', 'slug',)
    search_fields = ('name', 'slug',)
