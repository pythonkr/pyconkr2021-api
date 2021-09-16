from rest_framework import serializers

from program.models import Proposal


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['title', 'brief', 'desc', 'comment', 'difficulty',
                  'duration', 'language', 'category', 'introduction', 'video_url',
                  'slide_url'
                  ]
