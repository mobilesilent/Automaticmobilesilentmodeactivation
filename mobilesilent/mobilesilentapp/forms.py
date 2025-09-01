from django.forms import ModelForm
from mobilesilent.mobilesilentapp.models import Classroom, Complaints, Feedback, StudentTable, Timing
from mobilesilent.mobilesilentapp.views import Teacherregistration


class StuentForm(ModelForm):
    class Meta:
        model=StudentTable
        fields=['username','password','name','admission_no','department','class','semester','email','phone']
class ClassroomForm(ModelForm):
    class Meta:
        model=Classroom
        fields=['department','className','roomNumber']
class TimingForm(ModelForm):
    class Meta:
        model=Timing
        fields=['day','from','to','subject']
class FeedbackForm(ModelForm):
    class Meta:
        model=Feedback
        fields=['feedback']
class ComplaintsForm(ModelForm):
    class Meta:
        model=Complaints
        fields=['complaints','reply']
class TeacherregistrationForm(ModelForm):
    class Meta:
        model=Teacherregistration
        fields=['department','subject','phone']