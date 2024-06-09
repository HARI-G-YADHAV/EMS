
from django.contrib import admin
from .models import *
from exam.models import UserProfile
# Register your models here.
admin.site.register(Exam)
admin.site.register(ExamTimeTable)
admin.site.register(Programme)
admin.site.register(Department)
admin.site.register(preferTable)
admin.site.register(room)
admin.site.register(dutyAllotment)
admin.site.register(Course)
admin.site.register(teacherTable)
admin.site.register(Timetable)
admin.site.register(Optedtb)
