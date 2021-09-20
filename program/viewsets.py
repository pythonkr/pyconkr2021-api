from django.db.models import Q

from rest_framework import viewsets

from program.models import Proposal
from program.serializers import ProposalSerializer


class ProposalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Proposal.objects.all().order_by('video_open_at')
    serializer_class = ProposalSerializer
