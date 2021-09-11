from django.contrib.auth.models import User

from rest_framework import viewsets

from sponsor.serializers import UserSerializer, SponsorSerializer, SponsorLevelSerializer
from sponsor.models import Sponsor, SponsorLevel


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SponsorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorLevelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SponsorLevel.objects.all()
    serializer_class = SponsorLevelSerializer
