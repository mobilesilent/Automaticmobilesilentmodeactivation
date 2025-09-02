
from django.contrib import admin
from django.urls import include, path

from mobilesilentapp.views import *

urlpatterns = [
    path('',LoginPage.as_view(),name="LoginPage"),
    path('classroom',Classroom.as_view(),name="Classroom"),
    path('Timing',Timing.as_view(),name="Timing"),
    path('Register',Register.as_view(),name="Register"),
    path('Feedback',Feedback.as_view(),name="Feedback"),
    path('Complaints',Complaints.as_view(),name="Complaints"),
    path('Timetable',Timetable.as_view(),name="Timetable"),
    path('Teacherregistration',Teacherregistration.as_view(),name="Teacherregistration"),
    path('Admin_home',Admin_home.as_view(),name="Admin_home"),
    path('ManageClassroom',ManageClassroom.as_view(),name="ManageClassroom"),
    path('View_timetable',View_timetable.as_view(),name="View_timetable"),
    path('Select_class',Select_class.as_view(),name="Select_class"),
    path('Timetable_new',Timetable_new.as_view(),name="Timetable_new")

]
