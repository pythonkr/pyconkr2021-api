from django.contrib.auth.models import User

from rest_framework import viewsets

from api_2021.serializers import UserSerializer, SponsorSerializer
from api_2021.models import Sponsor


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
