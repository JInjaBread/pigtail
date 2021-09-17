from io import BytesIO
from PIL import Image

from django.db import models
from django.core.files import File
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, FileExtensionValidator
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


#Quiz and Assigment
class QuizCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)

    def __str__(self):
        return self.category
class QuestionsMultiplechoice(models.Model):
    question = models.CharField(max_length=255, unique=True, blank=False)
    a = models.CharField(max_length=255, blank=True)
    b = models.CharField(max_length=255, blank=True)
    c = models.CharField(max_length=255, blank=True)
    d = models.CharField(max_length=255, blank=True)
    c_answer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.question

class QuizMultipleChoice(models.Model):
    STATUS_CHOICE = [
        ('Hide', 'Hide'),
        ('Show', 'Show')
    ]

    status = models.CharField(max_length=255,choices=STATUS_CHOICE, default="Show")
    date_deadline = models.DateTimeField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    grades = models.PositiveIntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    questions = models.ManyToManyField(QuestionsMultiplechoice)

#Student User Models
class StudentUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    lrn = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(11)])
    section = models.ForeignKey(Section, default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

#Teacher User Models
class TeacherUser(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    assigned_subject = models.ManyToManyField(Subject, blank=False)

#Parents User Models
class ParentUser(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
