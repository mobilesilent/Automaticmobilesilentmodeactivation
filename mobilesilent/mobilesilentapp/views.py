from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from mobilesilentapp.forms import ClassroomForm
from mobilesilentapp.models import *

# Create your views here.
class LoginPage(View):
    def get(self,request):
        return render(request,"administration/login.html")    
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        try:
            obj = LoginTable.objects.get(username=username,password=password)
            request.session['user_id'] = obj.id

            # Handle based on user type
            if obj.user_type =='admin':
                return HttpResponse('''<script>alert("Wlcome back");window.location='/Admin_home'</script>''')
            else:
                return HttpResponse('''<script>alert("User not found");window.location='/'</sript>''')
        except LoginTable.DoesNotExist:
            # Handle case where login details do not exist
            return HttpResponse('''<script>alert("Invalid username or password");window.location='/'</script>''')    

class Classroom(View):
    def get(self,request):
        return render(request,"administration/classroom.html")
    def post(self,request):
        form=ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'administration/manageClassroom.html')
class Timing(View):
    def get(self,request):
            return render(request,"administration/timing.html")
class Register(View):
    def get(self,request):
        return render(request,"administration/register.html")
class Feedback(View):
    def get(self,request):
        return render(request,"administration/feedback.html")
class Complaints(View):
    def get(self,request):
        return render(request,"administration/complaints.html")
class Timetable(View):
    def get(self,request):
        return render(request,"administration/timetable.html")
class Teacherregistration(View):
    def get(self,request):
        return render(request,"administration/timetable.html") 
class Admin_home(View):
    def get(self,request):
        return render(request,"administration/admin_home.html")  
     
class ManageClassroom(View):
    def get(self,request):
        obj = ClassroomTable.objects.all()
        return render(request,"administration/manageClassroom.html", {'val':obj})
    
class ManageTimetable(View):
    def get(self,request):
        obj = Timing.objects.all()
        return render(request,"administration/manageTimetable.html")
class Select_class(View):
    def get(self,request):
        obj = Timing.objects.all()
        return render(request,"administration/select_class.html")
class View_timetable(View):
    def get(self,request):
       
        return render(request,"administration/View_timetable.html")
class Timetable_new(View):
    def get(self,request):
        obj = Timing.objects.all()
        return render(request,"administration/timetable_new.html")

