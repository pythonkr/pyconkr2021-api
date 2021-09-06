from django.contrib import admin

from log.models import Log


class LogAdmin(admin.ModelAdmin):
    readonly_fields = ('type', 'user', 'msg', 'ts', 'ip')
    list_display = ['type', 'user', 'ip', 'ts']
    ordering = ('-ts',)

    # Django Admin의 Action으로 삭제 불가능하도록 해당 Action을 Override
    def delete_queryset(self, request, queryset):
        new_log = Log()
        new_log.type = 'abnormal_action'
        new_log.user = request.user
        new_log.ip = request.META.get('REMOTE_ADDR')
        new_log.msg = '로그 삭제를 시도했습니다.'
        new_log.save()


admin.site.register(Log, LogAdmin)
