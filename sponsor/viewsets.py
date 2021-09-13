from django.contrib.auth.models import User

from rest_framework import viewsets

from sponsor.serializers import UserSerializer, SponsorSerializer, SponsorLevelSerializer, PatronSerializer
from sponsor.models import Sponsor, SponsorLevel, Patron


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SponsorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorLevelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SponsorLevel.objects.all().order_by('order')
    serializer_class = SponsorLevelSerializer


class PatronViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Patron.objects.all()
    serializer_class = PatronSerializer
