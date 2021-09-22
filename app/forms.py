from django import forms
from app.views import *

def check_for_name(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('name should not start with a character')

def check_for_name_limit(value):
    if len(value)>5:
        raise forms.ValidationError('name should not be more than 5 Charcters')

def check_for_age_limit(value):
    if value<18 or value>45:
        raise forms.ValidationError('Age Should be between 18 to 45')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_name,check_for_name_limit])
    age=forms.IntegerField(validators=[check_for_age_limit])
    email=forms.EmailField(max_length=100)
    reenteremail=forms.EmailField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    reenterpassword=forms.CharField(widget=forms.PasswordInput)
    bothcatcher=forms.CharField(widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['reenteremail']
        p=self.cleaned_data['password']
        rp=self.cleaned_data['reenterpassword']

        if e != r:
            raise forms.ValidationError('Both the emails are not matching')

        if p != rp:
            raise forms.ValidationError('Both the passwords are not matching')
        
    def clean_bothcatcher(self):
        b=self.cleaned_data['bothcatcher']

        if len(b)>=1:
            raise forms.ValidationError('bothcatcher is present')
        
