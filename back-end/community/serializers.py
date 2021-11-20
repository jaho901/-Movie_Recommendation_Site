from rest_framework import serializers
from .models import Community
from accounts.serializers import UserSerializer


class CommunitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Community
        fields = '__all__'