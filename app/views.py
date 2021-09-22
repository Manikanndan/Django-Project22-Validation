from django.http.response import HttpResponse
from django.shortcuts import render 
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def fun_student(request):
    form=StudentForm()
    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():
            return HttpResponse('Form Data Validated Successfully')
    return render(request,'student.html',context={'form':form})