from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth import get_user_model

from .models import User
from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
	# 1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
	# 1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
	# 2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
	# 3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후
        user.set_password(request.data.get('password'))
        user.save()
        # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다. (wrtie_only)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def user_delete(request):
    request.user.delete()
    return HttpResponse(status=200)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def follow(request, user_pk, other_pk):
    person = get_object_or_404(User, pk=user_pk)
    user = request.user
    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
            follow = True
        else:
            person.followers.add(user)
            follow = False
        follow_status = {
            'follow': follow,
            'followings': person.followings.count(),
            'followers': person.followers.count(),
            }
    else:
        if user.followers.filter(pk=other_pk).exists():
            user.followers.remove(request.user)
            follow = True
        follow_status = {
            'follow': follow,
            'followings': user.followings.count(),
            'followers': user.followers.count(),
        }
    return JsonResponse(follow_status)
    
