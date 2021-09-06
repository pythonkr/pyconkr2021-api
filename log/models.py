from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginLog(models.Model):
    type = models.CharField(max_length=20,
                            choices=(
                                ('', '---------'),
                                ('login', '로그인'),
                                ('logout', '로그아웃'),
                                ('login_fail', '실패')
                            ),
                            default='')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ip = models.GenericIPAddressField()
    msg = models.CharField(max_length=1000)
    ts = models.DateTimeField(auto_now_add=True)
