# Generated by Django 3.1.7 on 2021-09-15 03:26

import account.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20210915_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='photo',
            field=models.ImageField(default='default.jpeg', upload_to='uploads/', validators=[account.validators.validate_file_extension_image]),
        ),
    ]