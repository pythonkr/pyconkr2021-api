import datetime

from django.db.models.functions import Coalesce
from rest_framework.viewsets import ReadOnlyModelViewSet

from article.models import Article
from article.serializers import ArticleSerializer


class ArticleViewSet(ReadOnlyModelViewSet):
    queryset = Article.objects.filter(visible_at__lte=datetime.datetime.now()).order_by('-created_at')
    serializer_class = ArticleSerializer
