from django import forms
from finance.models import Blog



class Addblog(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'
