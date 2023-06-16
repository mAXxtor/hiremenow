from django.contrib import admin

from .models import Area, Company, Internship, InternshipField


# class InternshipFieldInline(admin.TabularInline):
#     model = InternshipsFields
#     min_num = 1


@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    """ Управление Стажировками """
    fields = ('name', 'short_description', 'start_date', 'end_date',
              'is_permanent', 'fields', 'company', 'created_at', 'updated_at',
              'published_at', 'visibility')
    search_fields = ('name', 'company__name')
    list_filter = ('name', 'visibility')
    list_display = ('name', 'fields', 'is_permanent', 'visibility')
    list_editable = ('is_permanent', 'visibility')
    readonly_fields = ('created_at', 'updated_at', 'published_at')
    # TODO Донастроить и убрать лишнее
    # fieldsets = ('get_internships_fields',)
    # inlines = (InternshipFieldInline,)

    # def get_internships_fields(self, internship):
    #     return [field.name for field in internship.fields.all()]


@admin.register(InternshipField)
class InternshipFieldAdmin(admin.ModelAdmin):
    """ Управление направлением стажировок """
    fields = ('name', 'slug')
    search_fields = ('name', 'slug')


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    """ Управление cферой деятельности организации """
    fields = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """ Управление организациями """
    fields = ('name', 'name_eng', 'slug', 'short_description', 'url_site',
              'url_vacancies', 'url_internships', 'url_tg_company',
              'url_tg_vacancies', 'url_tg_internships', 'logo', 'size',
              'areas')
    search_fields = ('name', 'slug')
