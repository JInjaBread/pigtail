# Generated by Django 3.1.7 on 2021-08-10 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20210810_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.section'),
        ),
    ]
