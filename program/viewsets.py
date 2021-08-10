from rest_framework import viewsets

from program.models import Proposal
from program.serializers import ProposalSerializer


class ProposalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
