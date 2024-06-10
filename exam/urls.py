from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.mylogin,name='login'),

    path('chief_dashboard/', views.chief_dashboard, name='chief_dashboard'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),


    path('exam/',views.exam,name='exam'),
    path('allot_duty/',views.allot_duty,name='allot_duty'),
    path('edit_teacher',views.edit_teacher,name='edit_teacher'),

    
]

