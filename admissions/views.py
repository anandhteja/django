from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from admissions.models import Student
from admissions.forms import Admissionform
from admissions.forms import Addnumbers
from django import forms
from django.views.generic import DetailView
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,View
from admissions.models import Teacher
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import User, auth

from django.contrib.auth.mixins import PermissionRequiredMixin

from finance.models import Blog
from admissions.forms import Updateprofile


# Create your views here.


@login_required(login_url='signin')
def addAdmissions(request):
    
    result=Admissionform
    admform={'form':result}
    if request.method=='POST':
        userinput=Admissionform(request.POST)
        if userinput.is_valid():

            n=userinput.cleaned_data['name']
            f=userinput.cleaned_data['father_name']
            c=userinput.cleaned_data['classname']


            response=render(request,'index.html')


            request.session['name']=n;
            request.session['father_name']=f;
            request.session['class_name']=c;
                            


                            
            userinput.save()

                                
            return response
                                    
                        
    return render(request,'admissions/addAdmissions.html',admform)


@login_required(login_url='signin')
def admissionReport(request):
    

    #get all the records from model
    result=Student.objects.all();
    #store it in a dictionary
    
    
                    
    
    
    students={'allstudents':result}
    
    
    return render(request,'admissions/admissionReport.html', students)




@login_required(login_url='signin')
def homepage(request):
    for k,v in request.session.items():
        if k in '_auth_user_id':
            id=v
            

            s=User.objects.get(id=id)
            dict={'user':s}
    return render(request,'index.html',dict)




@login_required(login_url='signin')
def addnumbers(request):
    

    result=Addnumbers
    add={'sumnumbers':result}
    if request.method=="POST":
        input=Addnumbers(request.POST)
        if input.is_valid():
            x=input.cleaned_data['number_1']
            y=input.cleaned_data['number_2']
            print(int(x)+int(y))
                
    return render(request,'admissions/addnumbers.html',add)

@login_required(login_url='signin')
@permission_required('admissions.delete_student')
def deletestudent(request,id):
    if not request.user.is_authenticated:
        return redirect('/')
    else:

        s=Student.objects.get(id=id)
        s.delete()
        return admissionReport(request)

@login_required(login_url='signin')
@permission_required('admissions.change_student')
def updatestudent(request,id):
    if not request.user.is_authenticated:
        return redirect('/')
    else:

        s=Student.objects.get(id=id)
        form=Admissionform(instance=s)
        dict={'form':form}
        if request.method=='POST':
            userinput=Admissionform(request.POST,instance=s)
            if userinput.is_valid():
                userinput.save()
                return admissionReport(request)
        return render(request,'admissions/updatestudent.html',dict)
        


class Teacherread(PermissionRequiredMixin,ListView):
    permission_required='admissions.view_teacher'
    model=Teacher




class Getteacher(DetailView):
    model=Teacher





class Insertteacher(CreateView):
    model=Teacher
    fields=('name', 'subject', 'contact_number')
    success_url=reverse_lazy('trreport')






class Updateteacher(PermissionRequiredMixin,UpdateView):
    permission_required='admissions.change_teacher'
    model=Teacher
    fields=('name','subject','contact_number')
    success_url=reverse_lazy('trreport')





class Deleteteacher(DeleteView):
    model=Teacher
    success_url=reverse_lazy('trreport')















def register(request):

    if request.method=='POST':
        n=request.POST['firstname']
        l=request.POST['lastname']
        u=request.POST['username']
        p1=request.POST['password1']
        p2=request.POST['password2']
        e=request.POST['email']


        


        if p1==p2:
            if User.objects.filter(username__in=[u]):
              return HttpResponse("<h1> Username already exists </h1>")
            elif User.objects.filter(email__in=[e]):
                return HttpResponse("<h1> Email already exists </h1>") 
            else:
                s=User.objects.create_user(username=u, password=p1,email=e,first_name=n, last_name=l)
                s.save()
            return redirect('signin')
        else:
            return HttpResponse("<h1>Passwords doesn't match</h1>")

        
        
    return render(request, 'admissions/register.html')




def signin(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['password']
        user=auth.authenticate(username=u, password=p)
        if user is not None:
            auth.login(request, user)
          
            request.session['username']=u
            
            return  redirect('home')



        else:
            return HttpResponse("<h1> Invalid credentials or Account doesn't exist")

    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='signin')
def deleteaccount(request):
    
    for k,v in request.session.items():
        if k in '_auth_user_id':
            id=v
            

            s=User.objects.get(id=id)
            

            s.delete()
            return HttpResponse("<h1> Account deleted successfully</h1>")




def updateprofile(request):
    
    for k,v in request.session.items():
        if k in '_auth_user_id':
            id=v
            s=User.objects.get(id=id)
            form=Updateprofile(instance=s)
            dict={'form':form}
            if request.method=='POST':
                userinput=Updateprofile(request.POST,instance=s)
                if userinput.is_valid():
                    userinput.save()
                    return admissionReport(request)
            
            return render(request, 'admissions/updateprofile.html',dict)


    