from django import forms

from admissions.models import Student
from django.contrib.auth.models import User, auth




class Admissionform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'



class Addnumbers(forms.Form):
    number_1=forms.CharField()
    number_2=forms.CharField()



class Updateprofile(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name', 'last_name','email', 'username')


