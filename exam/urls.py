from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.mylogin,name='login'),

    path('chief_dashboard/', views.chief_dashboard, name='chief_dashboard'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),


    path('exam_view/',views.exam,name='exam_view'),
    path('get-courses/', views.get_courses, name='get_courses'),

    path('allot_duty/',views.allot_duty,name='allot_duty'),
    path('edit_teacher',views.edit_teacher,name='edit_teacher'),

    path('uploading_preference/', views.exam_table, name='uploading_preference'),
    path('announce_exam/', views.announce_exam, name='announceExam'),

    
]

