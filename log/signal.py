from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

from log.models import Log


@receiver(user_logged_in)
def sig_user_logged_in(sender, user, request, **kwargs):
    new_log = Log()
    new_log.type = 'login'
    new_log.user = user
    new_log.ip = request.META.get('REMOTE_ADDR')
    new_log.save()


@receiver(user_logged_out)
def sig_user_logged_out(sender, user, request, **kwargs):
    new_log = Log()
    new_log.type = 'logout'
    new_log.user = user
    new_log.ip = request.META.get('REMOTE_ADDR')
    new_log.save()


@receiver(user_login_failed)
def sig_user_login_failed(sender, user, request, **kwargs):
    new_log = Log()
    new_log.type = 'login_fail'
    new_log.user = user
    new_log.ip = request.META.get('REMOTE_ADDR')
    new_log.save()
