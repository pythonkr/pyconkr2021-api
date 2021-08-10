from django.contrib.auth.models import User

from rest_framework import viewsets

from sponsor.serializers import UserSerializer, SponsorSerializer
from sponsor.models import Sponsor


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SponsorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
