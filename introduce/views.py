from django.shortcuts import render
from introduce.models import Admin_AccessLog

# Create your views here.
def introduce(request):
    access_log = Admin_AccessLog()
    access_log.location = "introduce"
    access_log.save()
    return render(request,'introduce.html')