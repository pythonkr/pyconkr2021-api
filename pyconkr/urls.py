"""pyconkr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


from rest_framework import routers

from sponsor.viewsets import SponsorViewSet, SponsorLevelViewSet, PatronViewSet, SponsorDetailViewSet
from program.viewsets import ProposalViewSet
from article.viewsets import ArticleViewSet

from program.views import SessionListApi

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'sponsors', SponsorLevelViewSet)
# router.register(r'program', ProposalViewSet)
router.register(r'article', ArticleViewSet)
router.register(r'patron', PatronViewSet)
# router.register(r'sponsor_detail', SponsorDetailViewSet)

urlpatterns = [
    path('health', lambda request: HttpResponse('good')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # API
    path('api/v1/program/', SessionListApi.as_view()),

    # DRF Router
    path('api/v1/', include(router.urls)),
]
