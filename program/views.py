from django.shortcuts import render
from django.db.models import Q

from rest_framework import generics, mixins
from rest_framework.response import Response

import rest_framework.status as status

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

        return queryset.order_by('video_open_at', 'track_num')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(self.serializer_class(queryset, many=True).data)


class SessionDetailApi(generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        try:
            queryset = Proposal.objects.get(id=kwargs['id'])
        except Proposal.DoesNotExist:
            return Response({'msg': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProposalSerializer(queryset, many=False)

        return Response(serializer.data)
