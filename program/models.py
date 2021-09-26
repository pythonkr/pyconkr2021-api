from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class ProgramCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Proposal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=255)
    brief = models.TextField(max_length=1000)
    desc = models.TextField(max_length=4000)
    comment = models.TextField(max_length=4000, null=True, blank=True)

    difficulty = models.CharField(max_length=1,
                                  choices=(
                                      ('B', _('Beginner')),
                                      ('I', _('Intermediate')),
                                      ('E', _('Experienced')),
                                  ))

    duration = models.CharField(max_length=1,
                                choices=(
                                    ('S', _('15min')),
                                    ('L', _('30min')),
                                ))

    language = models.CharField(max_length=1,
                                choices=(
                                    ('', '---------'),
                                    ('K', _('Korean')),
                                    ('E', _('English')),
                                ),
                                default='')

    category = models.ForeignKey(
        ProgramCategory, on_delete=models.SET_DEFAULT, null=True, blank=True, default=14)
    accepted = models.BooleanField(default=False)
    introduction = models.TextField(max_length=1000, null=True, blank=True,
                                    help_text=_('발표 소개 페이지에 들어가는 내용입니다. 변경 사항은 최대 60분 이내에 적용됩니다.'))
    video_url = models.CharField(max_length=255, null=True, blank=True, help_text=_('발표 영상 URL'))
    slide_url = models.CharField(max_length=255, null=True, blank=True, help_text=_('발표 자료 URL'))
    video_open_at = models.DateTimeField(null=True, blank=True, help_text=_('파이콘 한국 유튜브에 공개되는 시간'))
    track_num = models.IntegerField(null=True, blank=True, help_text=_('트랙 번호'))

    def __str__(self):
        return self.title
