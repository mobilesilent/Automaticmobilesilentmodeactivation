from django.forms import ModelForm
from mobilesilentapp.models import ClassroomTable, Complaints, Feedback, StudentTable, TeacherTable, Timing



class StuentForm(ModelForm):
    class Meta:
        model=StudentTable
        fields=['name','admission_no','department','class_name','semester','email_id','phone_no']
class ClassroomForm(ModelForm):
    class Meta:
        model=ClassroomTable
        fields=['department','className','roomNumber']
class TimingForm(ModelForm):
    class Meta:
        model=Timing
        fields=['day','start','to','subject']
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
        model=TeacherTable
        fields=['department','subject','phone_no']