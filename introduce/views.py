from django.shortcuts import render
import logging

logger = logging.getLogger('mylogger')
def first_view(request):
    return render(request,'introduce.html')
# Create your views here.
