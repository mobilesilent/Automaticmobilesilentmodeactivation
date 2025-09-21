
from django.contrib import admin
from django.urls import include, path

from mobilesilentapp.views import *

urlpatterns = [

    path('',LoginPage.as_view(),name="LoginPage"),

    # /////////////////////////////// ADMIN //////////////////////////////////////////////////////////
    path('ManageClassroom',ManageClassroom.as_view(),name="ManageClassroom"),
    path('classroom',Classroom.as_view(),name="Classroom"),
    path('ManageDepartment',ManageDepartment.as_view(),name="ManageDepartment"),
    path('AddDepartment',AddDepartment.as_view(),name="AddDepartment"),
    path('Complaints',Complaints.as_view(),name="Complaints"),
    path('Reply/<int:c_id>',Reply.as_view(),name="Reply"),
    path('Feedback',Feedback.as_view(),name="Feedback"),
    path('teacher',TeacherView.as_view(),name="teacher"),
    path('acceptteacher/<int:id>', AcceptTeacher.as_view()),
    path('rejectteacher/<int:id>', RejectTeacher.as_view()),





# ////////////////////////////////////////////////////////////////////////////////////////////////




    path('Timing',Timing.as_view(),name="Timing"),
    path('TeacherRegister',TeacherRegister.as_view(),name="TeacherRegister"),
    path('Timetable',Timetable.as_view(),name="Timetable"),
    path('Teacherregistration',Teacherregistration.as_view(),name="Teacherregistration"),
    path('Admin_home',Admin_home.as_view(),name="Admin_home"),
    path('View_timetable',View_timetable.as_view(),name="View_timetable"),
    path('Select_class',Select_class.as_view(),name="Select_class"),
    path('Timetable_new',Timetable_new.as_view(),name="Timetable_new"),
    path('ManageTeacher',ManageTeacher.as_view(),name="ManageTeacher"),
    path('DeleteDepartment/<int:id>',DeleteDepartment.as_view(),name="DeleteDepartment"),
    path('DeleteClassroom/<int:id>',DeleteClassroom.as_view(),name="DeleteClassroom"),

]
