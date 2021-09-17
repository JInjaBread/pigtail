# Generated by Django 3.1.7 on 2021-09-15 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20210915_0101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('category',)},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='slug',
            field=models.SlugField(default=2),
            preserve_default=False,
        ),
    ]