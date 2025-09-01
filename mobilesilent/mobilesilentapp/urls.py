
from django.contrib import admin
from django.urls import include, path

from mobilesilentapp.views import *

urlpatterns = [
    path('',LoginPage.as_view(),name="LoginPage"),
    path('Classroom',Classroom.as_view(),name="Classroom"),
    path('Timing',Timing.as_view(),name="Timing"),
    path('Register',Register.as_view(),name="Register"),
    path('Feedback',Feedback.as_view(),name="Feedback"),
    path('Complaints',Complaints.as_view(),name="Complaints"),
    path('Timetable',Timetable.as_view(),name="Timetable"),
    path('Teacherregistration',Teacherregistration.as_view(),name="Teacherregistration"),
    path('Admin_home',Admin_home.as_view(),name="Admin_home"),
    path('ManageClassroom',ManageClassroom.as_view(),name="ManageClassroom"),
]
