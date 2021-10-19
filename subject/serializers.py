from rest_framework import serializers
from .models import *

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

#quiz serializers

class QuestionsMultiplechoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuestionsMultiplechoice
        fields = ('question', 'a', 'b', 'c', 'd', 'c_answer')

class QuizTrueFalseSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuizTrueFalse
        fields = ('question', 'c_answer')

class QuizParagraphSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuizParagraph
        fields = ('question', 'answer')

class Quiz(serializers.ModelSerializer):
    multiple_choice = QuestionsMultiplechoiceSerializers(read_only=True, many=True)
    true_false = QuizTrueFalseSerializers(read_only=True, many=True)
    quiz_paragraph = QuizParagraphSerializers(read_only=True, many=True)
    class Meta:
        model = Quiz
        fields = ('status', )
