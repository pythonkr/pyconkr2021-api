from django.contrib import admin
from django.db import models
from django import forms

from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportModelAdmin

from pyconkr.summernote import SummernoteWidgetWithCustomToolbar

from .models import Proposal, ProgramCategory


class ProgramCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(ProgramCategory, ProgramCategoryAdmin)


class ProgramAdmin(SummernoteModelAdmin):
    formfield_overrides = {models.TextField: {
        'widget': SummernoteWidgetWithCustomToolbar}
    }

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super(ProgramAdmin, self).get_queryset(request)
        else:
            return Proposal.objects.filter(user=request.user)

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
            kwargs['exclude'] = ['user', 'difficulty', 'duration', 'language', 'category',
                                 'accepted', 'introduction', 'video_url', 'slide_url', 'video_open_at',
                                 'track_num', 'title']

        return super().get_form(request, obj=None, change=False, **kwargs)


admin.site.register(Proposal, ProgramAdmin)
