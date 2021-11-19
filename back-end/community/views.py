from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from django.shortcuts import get_object_or_404

from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Community
from .serializers import CommunitySerializer

@api_view(['GET'])
def community_list(request):
    community_li = Community.objects.all()
    serializer = CommunitySerializer(community_li, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def community_create(request):
    serializer = CommunitySerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(use=request.user)
        return Response(serializer.data)

