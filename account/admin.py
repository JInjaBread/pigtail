from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Module)
admin.site.register(Subject)
admin.site.register(Section)
admin.site.register(StudentUser)
admin.site.register(QuizCategory)
admin.site.register(QuestionsMultiplechoice)
admin.site.register(QuizMultiplchoice)
