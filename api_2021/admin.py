from django.contrib import admin
from django.db import models
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Sponsor, SponsorLevel

from django_summernote.widgets import SummernoteWidget


class SummernoteWidgetWithCustomToolbar(SummernoteWidget, ImportExportModelAdmin):
    def template_contexts(self):
        contexts = super(SummernoteWidgetWithCustomToolbar,
                         self).template_contexts()
        contexts['width'] = '960px'
        return contexts


class SponsorAdmin(SummernoteModelAdmin, ImportExportModelAdmin):
    formfield_overrides = {models.TextField: {
        'widget': SummernoteWidgetWithCustomToolbar}}
    autocomplete_fields = ('creator', 'manager_id',)
    list_display = ('creator', 'name', 'level', 'manager_name', 'manager_email', 'manager_id',
                    'submitted', 'accepted', 'paid_at',)
    list_filter = ('accepted',)
    ordering = ('-created_at',)


admin.site.register(Sponsor, SponsorAdmin)


class SponsorLevelAdmin(SummernoteModelAdmin):
    list_display = ('id', 'order', 'name', 'slug', 'price', 'limit',)
    list_editable = ('order', 'slug',)
    ordering = ('order',)
    search_fields = ('name',)


admin.site.register(SponsorLevel, SponsorLevelAdmin)
