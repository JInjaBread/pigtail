# Generated by Django 3.1.7 on 2021-06-10 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='subjects',
        ),
        migrations.AddField(
            model_name='section',
            name='subjects',
            field=models.ManyToManyField(to='account.Subject'),
        ),
    ]
