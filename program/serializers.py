from rest_framework import serializers

from program.models import Proposal, ProgramCategory


class ProposalSerializer(serializers.ModelSerializer):
    video_open_at = serializers.DateTimeField(format='%m/%d %H:%M')
    difficulty = serializers.ChoiceField(choices=(
                                      ('B', 'Beginner'),
                                      ('I', 'Intermediate'),
                                      ('E', 'Experienced'),
                                  ))
    duration = serializers.ChoiceField(choices=(
                                    ('S', '15min'),
                                    ('L', '30min'),
                                ))
    category = serializers.StringRelatedField()

    class Meta:
        model = Proposal
        fields = ['title', 'brief', 'desc', 'comment', 'difficulty',
                  'duration', 'language', 'category', 'introduction', 'video_url',
                  'slide_url', 'video_open_at', 'user_name', 'id',
                  ]
