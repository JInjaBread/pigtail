from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import *
from account.models import StudentUser
from .serializers import SubjectSerializers
from account.serializers import StudentSerializers

# API views for Student.
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
