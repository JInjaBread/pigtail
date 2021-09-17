from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import *


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name')

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'groups',)

#Student Serializers

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category',)

class ModuleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('name', 'get_modules',)

class SectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('section_name', )

class SubjectSerializers(serializers.ModelSerializer):
        module = ModuleSerializers(read_only=True, many=True)
        category = CategorySerializers(read_only=True, many=False)
        section = SectionSerializers(read_only=True, many=False)
        class Meta:
            model = Subject
            fields = ('name','get_photo', 'category', 'module', 'channel', 'section')

class StudentSerializers(serializers.ModelSerializer):
    #get the source from object
    def getUsername(self, obj):
        return obj.user.username

    def getEmail(self, obj):
        return obj.user.email

    def getFirstname(self, obj):
        return obj.user.first_name

    def getLastname(self, obj):
        return obj.user.last_name

    #pass to serializers
    username = serializers.SerializerMethodField("getUsername")
    email = serializers.SerializerMethodField("getEmail")
    first_name = serializers.SerializerMethodField("getFirstname")
    last_name = serializers.SerializerMethodField("getLastname")
    section = SectionSerializers(read_only=True, many=False)
    class Meta:
        model = StudentUser
        fields = ('user','username','email', 'lrn','first_name','last_name', 'section')
