from django.contrib import admin

from mobilesilentapp.models import *

# Register your models here.
admin.site.register(LoginTable),
admin.site.register(StudentTable),
admin.site.register(Classroom),
admin.site.register(Timing),
admin.site.register(Feedback),
admin.site.register(Complaints),
admin.site.register(TeacherTable)