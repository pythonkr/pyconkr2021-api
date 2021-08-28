from django.contrib import admin

from article.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'visible_at',)


admin.site.register(Article, ArticleAdmin)
