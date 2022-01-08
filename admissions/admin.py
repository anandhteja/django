from django.contrib import admin
from admissions.models import Student
from finance.models import Fee
from finance.models import Blog
from admissions.models import Teacher,About


# Register your models here.


class Studentadmin(admin.ModelAdmin):
    list_display=['id','name','father_name','classname','contact_number']



admin.site.register(Student,Studentadmin)  

class Feeadmin(admin.ModelAdmin):
    list_display=['id','Student_name','father_name','class_name','contact_number','fee_due']

admin.site.register(Fee,Feeadmin)   

class Studentblog(admin.ModelAdmin):
    list_display=['title','description','created','photo']

admin.site.register(Blog,Studentblog)




class Teacheradmin(admin.ModelAdmin):
    list_display=['id','name','subject','contact_number']
admin.site.register(Teacher,Teacheradmin)





#class Aboutadmin(admin.ModelAdmin):
    #list_display=['name','email','phone','message']

admin.site.register(About)




