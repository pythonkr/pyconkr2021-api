from datetime import datetime, timezone, timedelta

from django.db.models.functions import Coalesce
from rest_framework.viewsets import ReadOnlyModelViewSet

from article.models import Article
from article.serializers import ArticleSerializer


KST = timezone(timedelta(hours=0))


class ArticleViewSet(ReadOnlyModelViewSet):
    queryset = Article.objects.filter(visible_at__lte=datetime.now(tz=KST)).order_by('-created_at')
    serializer_class = ArticleSerializer

    # datetime 객체의 동적생성을 위해 get_queryset override (상단의 queryset은 무시됨)
    def get_queryset(self):
        return Article.objects.filter(visible_at__lte=datetime.now(tz=KST)).order_by('-created_at')
