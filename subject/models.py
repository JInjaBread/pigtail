from django.db import models
from .validators import validate_file_extension_image, validate_file_extension_pdf
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255, unique=True, blank=False)
    slug = models.SlugField()

    class Meta:
        ordering = ('category', )

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Module(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    module = models.FileField(upload_to='uploads/Modules', validators=[validate_file_extension_pdf])

    def get_modules(self):
        if self.module:
            return 'http://127.0.0.1:8000' + self.module.url
        return ""

    def __str__(self):
            return self.name

class Section(models.Model):
    section_name = models.CharField(max_length=255, unique=True, default="", null=False)

    def __str__(self):
        return self.section_name

class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    slug = models.SlugField()
    photo = models.ImageField(default="default.jpeg", upload_to='uploads/', validators=[validate_file_extension_image])
    category = models.ForeignKey(Category, default="", on_delete=models.CASCADE)
    modules = models.ManyToManyField(Module, blank=False)
    channel = models.CharField(max_length=255, unique=True, default="xxx", null=False)
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    grades = models.PositiveIntegerField(default="100")

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/self.category.slug/{self.slug}/'

    def get_photo(self):
        if self.photo:
            return 'http://127.0.0.1:8000' + self.photo.url
        return ''

#Quiz and Assigment.
class QuestionsMultiplechoice(models.Model):
    question = models.CharField(max_length=255, unique=True, blank=False)
    a = models.CharField(max_length=255, blank=True)
    b = models.CharField(max_length=255, blank=True)
    c = models.CharField(max_length=255, blank=True)
    d = models.CharField(max_length=255, blank=True)
    c_answer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.question

class QuizTrueFalse(models.Model):
    CHOICE = [
        ('True', 'True'),
        ('False', 'False')
    ]
    question = models.CharField(max_length=255, unique=True, blank=False)
    c_answer = models.CharField(max_length=255, choices=CHOICE)

    def __str__(self):
        return self.question

class QuizParagraph(models.Model):
    question = models.CharField(max_length=255, unique=True, blank=False)
    answer = models.CharField(max_length=2000, unique=True, blank=True)

    def __str__(self):
        return self.question

class Quiz(models.Model):
    STATUS_CHOICE = [
        ('Hide', 'Hide'),
        ('Show', 'Show')
    ]

    status = models.CharField(max_length=255,choices=STATUS_CHOICE, default="Hide")
    date_deadline = models.DateTimeField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    grades = models.PositiveIntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    multiple_choice = models.ManyToManyField(QuestionsMultiplechoice)
    true_false = models.ManyToManyField(QuizTrueFalse)
    quiz_paragraph = models.ManyToManyField(QuizParagraph)

    def __str__(self):
        return self.status
