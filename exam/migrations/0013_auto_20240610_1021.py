# Generated by Django 3.2.12 on 2024-06-10 10:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0012_delete_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='exam_id',
        ),
        migrations.AddField(
            model_name='timetable',
            name='course_code',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='timetable',
            name='department',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='timetable',
            name='exam',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='timetable',
            name='time_from',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='timetable',
            name='time_to',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
