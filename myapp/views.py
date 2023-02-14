from django.shortcuts import render
from myapp.forms import autherform
from django.contrib import messages
from myapp.models import auther
# Create your views here.

def autheinfo(request):
    if request.method=='POST':
        form=autherform(request.POST)
        if form.is_valid():
            messages.info(request,"data recorded succefully")
            form.save()
    else:
        form=autherform()
    auth=auther.objects.all()
    return render(request,'auther.html',{'form':form,'auth':auth})
