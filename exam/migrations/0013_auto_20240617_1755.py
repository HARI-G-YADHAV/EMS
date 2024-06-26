# Generated by Django 3.2.12 on 2024-06-17 17:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam', '0012_auto_20240617_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dutyallotment',
            old_name='exam_id',
            new_name='course_id',
        ),
        migrations.RemoveField(
            model_name='dutyallotment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='prefertable',
            name='exam_id',
        ),
        migrations.AddField(
            model_name='prefertable',
            name='course_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='exam.examtimetable'),
        ),
        migrations.AlterField(
            model_name='dutyallotment',
            name='teacher_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='exam.teachertable'),
        ),
        migrations.AlterField(
            model_name='prefertable',
            name='teacher_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
