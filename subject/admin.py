from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Module)
admin.site.register(Subject)
admin.site.register(Section)
admin.site.register(QuestionsMultiplechoice)
admin.site.register(QuizTrueFalse)
admin.site.register(QuizParagraph)
admin.site.register(Quiz)
