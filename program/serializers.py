from rest_framework import serializers

from program.models import Proposal, ProgramCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramCategory
        fields = ['id', 'name']


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
    category_data = serializers.SerializerMethodField()

    def get_category_data(self, obj):
        return CategorySerializer(obj.category).data

    class Meta:
        model = Proposal
        fields = ['title', 'brief', 'desc', 'comment', 'difficulty',
                  'duration', 'language', 'category', 'introduction', 'video_url',
                  'slide_url', 'video_open_at', 'user_name', 'id',
                  'category_data'
                  ]
