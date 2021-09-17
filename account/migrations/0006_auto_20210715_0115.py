# Generated by Django 3.1.7 on 2021-07-15 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210710_0335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='subjects',
        ),
        migrations.AddField(
            model_name='subject',
            name='section',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='account.section'),
        ),
    ]
