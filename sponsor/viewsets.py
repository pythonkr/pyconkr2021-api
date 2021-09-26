from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response

from sponsor.serializers import UserSerializer, SponsorSerializer, SponsorLevelSerializer, PatronSerializer
from sponsor.models import Sponsor, SponsorLevel, Patron


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SponsorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsorDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = Sponsor.objects.get(slug=kwargs['pk'])
        serializer = SponsorSerializer(queryset, many=False)

        return Response(serializer.data)


class SponsorLevelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SponsorLevel.objects.all().order_by('order')
    serializer_class = SponsorLevelSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            queryset = Sponsor.objects.get(slug=kwargs['pk'])
        except Sponsor.DoesNotExist:
            return Response({'msg': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SponsorSerializer(queryset, many=False)

        return Response(serializer.data)



class PatronViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Patron.objects.all()
    serializer_class = PatronSerializer
