# Generated by Django 3.2.12 on 2024-06-15 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_course_lab_theory'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='date',
            field=models.DateField(default='2020-01-01'),
        ),
    ]
