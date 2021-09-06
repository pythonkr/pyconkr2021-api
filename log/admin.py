from django.contrib import admin

from log.models import Log


class LogAdmin(admin.ModelAdmin):
    readonly_fields = ('type', 'user', 'msg', 'ts', 'ip')
    list_display = ['type', 'user', 'ip', 'ts']
    ordering = ('-ts',)

    # Django Admin의 Action으로 삭제 불가능하도록 해당 Action을 Override
    def delete_queryset(self, request, queryset):
        pass


admin.site.register(Log, LogAdmin)
