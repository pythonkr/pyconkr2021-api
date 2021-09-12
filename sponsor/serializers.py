from django.contrib.auth.models import User

from rest_framework import serializers

from sponsor import models


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sponsor
        fields = ['name', 'desc', 'logo_image']


class SponsorLevelSerializer(serializers.ModelSerializer):
    sponsors = SponsorSerializer(many=True)

    class Meta:
        model = models.SponsorLevel
        fields = ['name', 'sponsors']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class PatronSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patron
        fields = ('user_name', 'desc', )
