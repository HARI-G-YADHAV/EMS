from django import forms
from .models import preferTable, Course
from .models import  Department
from .models import Exam

# class ExamTimeTable(forms.ModelForm):
#      class Meta:
#          model = ExamTimeTable
#          fields = [ 'dept', 'date', 'time_from', 'time_to','semester', 'course_id']


class PreferTableForm(forms.ModelForm):
     exam_date = forms.DateField(widget=forms.Select())

     class Meta:
         model = preferTable
         fields = ['exam_date']

class CourseAdminForm(forms.ModelForm):
     csv_file = forms.FileField()

     class Meta:
         model = Course
         fields = '__all__'


class ExamAnnounce(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['sem', 'year', 'month', 'grad_level', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'grad_level': forms.Select(choices=[
                ('UG', 'Undergraduate (UG)'),
                ('PG', 'Postgraduate (PG)'),
                ('Int MSc', 'Integrated MSc')
            ])
        }



