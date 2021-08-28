from datetime import datetime, timezone, timedelta

from django.db.models.functions import Coalesce
from rest_framework.viewsets import ReadOnlyModelViewSet

from article.models import Article
from article.serializers import ArticleSerializer


KST = timezone(timedelta(hours=9))


class ArticleViewSet(ReadOnlyModelViewSet):
    queryset = Article.objects.filter(visible_at__lte=datetime.now(tz=KST)).order_by('-created_at')
    serializer_class = ArticleSerializer
