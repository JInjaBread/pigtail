from django.shortcuts import render
from django.http import Http404

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import *
from .serializers import StudentSerializers, SubjectSerializers


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

#API views for Student

class StudentAPIVIEW(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        userid = request.user.id
        student_user = StudentUser.objects.get(user=userid)
        section_id = student_user.section.id
        subject = Subject.objects.filter(section=section_id)
        serializers_subject = SubjectSerializers(subject, many=True)
        serializers_user = StudentSerializers(student_user, many=False)
        return Response(serializers_user.data)

class StudentSubjectAPIVIEW(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        userid = request.user.id
        student_user = StudentUser.objects.get(user=userid)
        section_id = student_user.section.id
        subject = Subject.objects.filter(section=section_id)
        serializers_subject = SubjectSerializers(subject, many=True)
        return Response(serializers_subject.data)
