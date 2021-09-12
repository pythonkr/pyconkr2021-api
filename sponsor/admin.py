from django.contrib import admin
from django.db import models
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Sponsor, SponsorLevel, Patron

from pyconkr.summernote import SummernoteWidgetWithCustomToolbar


class SponsorAdmin(SummernoteModelAdmin, ImportExportModelAdmin):
    formfield_overrides = {models.TextField: {
        'widget': SummernoteWidgetWithCustomToolbar}}
    autocomplete_fields = ('creator', 'manager_id',)
    list_display = ('creator', 'name', 'level', 'manager_name', 'manager_email', 'manager_id',
                    'submitted', 'accepted', 'paid_at',)
    list_filter = ('accepted',)
    ordering = ('-created_at',)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super(SponsorAdmin, self).get_queryset(request)
        else:
            return Sponsor.objects.filter(creator=request.user) | Sponsor.objects.filter(manager_id=request.user)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def get_form(self, request, obj=None, change=False, **kwargs):
        if not request.user.is_superuser:
            kwargs['exclude'] = ['slug', 'creator', 'name', 'level', 'manager_name',
                                 'manager_email', 'manager_id', 'submitted', 'accepted', 'paid_at',]

        return super().get_form(request, obj=None, change=False, **kwargs)


admin.site.register(Sponsor, SponsorAdmin)


class SponsorLevelAdmin(SummernoteModelAdmin):
    list_display = ('id', 'order', 'name', 'slug', 'price', 'limit',)
    list_editable = ('order', 'slug',)
    ordering = ('order',)
    search_fields = ('name',)


admin.site.register(SponsorLevel, SponsorLevelAdmin)


class PatronAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'price', 'desc',)


admin.site.register(Patron, PatronAdmin)
