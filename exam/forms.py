# forms.py
from django import forms
from .models import Timetable

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['exam', 'course_code', 'department', 'date', 'time_from', 'time_to']
