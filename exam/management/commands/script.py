# myapp/management/commands/import_data.py

from django.core.management.base import BaseCommand
from exam.models import Course, Department
import pandas as pd

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def handle(self, *args, **options):
        # Your data importing logic here
        csv_file_path = '~/Desktop/PROJECT/EMS/data/data1.csv'
        df = pd.read_csv(csv_file_path)

        for index, row in df.iterrows():
            print(f"{row=}")
            course = Course(
                course_id=row['course_id'],
                course_title=row['course_title'],
                course_code=row['course_code'],
                dept=Department.objects.get(dept_id=row['dept_id']),
                syllabus_year=row['syllabus_intro_year'],
                semester = row['semester'],
                lab_theory=row['lab_theory'],
                grad_level = row['grad_level']
            )
            course.save()

        self.stdout.write(self.style.SUCCESS('Data import completed.'))

