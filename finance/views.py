from django.shortcuts import render,redirect
from django.http import HttpResponse
from finance.models import Fee
from finance.models import Blog
from finance.forms import Addblog

from admissions.views import homepage

from django.db.models import Avg,Sum, Min,Max,Count

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
# Create your views here.





def Feecollection(request):
    result=Fee.objects.all()
    studentfees={'feecollection':result}
    return render(request,'finance/feeCollection.html',studentfees)




def Feecollection_10(request):

    
    result=Fee.objects.filter(class_name__in=[10]).order_by('Student_name','fee_due')




    studentfees={'feecollection':result}

    return render(request,'finance/feeCollection_10.html',studentfees);

def Feecollection_8(request):
    result=Fee.objects.filter(class_name__in=[8]) 
    studentfees={'feecollection':result}
    return render(request,'finance/feeCollection_8.html',studentfees)
    

def Registration(request):
    return render(request,'finance/RegistrationForm.html')


def feeDuesReport(request):
    return HttpResponse("<h1>i'll get fees dues from this view</h1>")



def feeCollectionReport(request):
    return HttpResponse("<h1>i'll get fees collection report from this view</h1>")






def selectclass(request):
    return render(request,'finance/select class.html')



    

def addblog(request):
    if request.method == 'POST':
        form = Addblog(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return homepage(request)
    else:
        form = Addblog
    return render(request,'finance/blog.html',{'form' : form})






def viewblog(request):
    result=Blog.objects.all()
    dict={'data':result}
    return render(request,'finance/viewblog.html',dict)


