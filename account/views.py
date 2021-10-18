from django.shortcuts import render
from django.http import Http404

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import *


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        return {
            "username": self.user.username,
            "email": self.user.email,
            "permissions": self.user.user_permissions.values_list("codename", flat=True),
            "groups": self.user.groups.values_list("name", flat=True),
            **attrs,
        }


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
