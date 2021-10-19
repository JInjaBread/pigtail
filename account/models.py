import os
from io import BytesIO
from PIL import Image

from django.db import models
from django.conf import settings
from django.core.files import File
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from subject.models import Section, Subject
from subject.validators import validate_file_extension_image
#Student User Models
def user_directory_path(instance, filename):
    profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_pic_name

class StudentUser(models.Model):
    GENDER_CHOICE = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    photo = models.ImageField(default="default.jpeg", upload_to=user_directory_path, validators=[validate_file_extension_image])
    gender = models.CharField(max_length=255, null=True, choices=GENDER_CHOICE)
    lrn = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(11)])
    section = models.ForeignKey(Section, default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def get_photo(self):
        if self.photo:
            return 'http://127.0.0.1:8000' + self.photo.url
        return ''

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        SIZE = 128, 128

        if self.photo:
            pic = Image.open(self.photo.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.photo.path)


#Teacher User Models
class TeacherUser(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    assigned_subject = models.ManyToManyField(Subject, blank=False)

#Parents User Models
class ParentUser(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
