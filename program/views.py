from django.shortcuts import render
from django.db.models import Q

from rest_framework import generics
from rest_framework.response import Response

from program.serializers import ProposalSerializer
from program.models import Proposal


class SessionListApi(generics.ListAPIView):
    serializer_class = ProposalSerializer

    def get_queryset(self):
        queryset = Proposal.objects.none()

        if 'day' not in self.request.GET:
            queryset = Proposal.objects.all()
        elif self.request.GET['day'] not in ('2', '3'):
            queryset = Proposal.objects.none()
        else:
            queryset = Proposal.objects.filter(
                Q(video_open_at__month='10'),
                Q(video_open_at__day=self.request.GET['day'])
            )

        return queryset.order_by('video_open_at')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(self.serializer_class(queryset, many=True).data)
