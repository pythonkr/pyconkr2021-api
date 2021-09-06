from django.contrib import admin

from log.models import Log


class LogAdmin(admin.ModelAdmin):
    readonly_fields = ('type', 'user', 'msg', 'ts',)
    list_display = ['type', 'user', 'ip', 'ts']
    ordering = ('-ts',)


admin.site.register(Log, LogAdmin)
