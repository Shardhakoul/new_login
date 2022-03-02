#registration form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import *

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label = 'Please enter your usual email address.',
        max_length = 55,
        required = True,
        widget = forms.EmailInput)# to add more boostrap features or calss use attrs={'class':'form-control'}
    first_name = forms.CharField(max_length=100,required=True)
    last_name = forms.CharField(max_length=100,required=True)
    phone = forms.CharField(label = 'Please enter your phone number without country code')
    #use pincodes instead of full add ? ref- prof's elderly inclass ref.
    wadd = forms.CharField(label = 'Enter Your Work Address ',max_length=5,required=True)
    #same note as wadd.
    hadd = forms.CharField(label = 'Enter Your Home Address ',max_length=5,required=True)
    #dob = forms.DateField(required=True)
    #better to take bool ? ref - ease of use.
    Vaccinated = forms.BooleanField(label = 'Are you vaccinated ?',required=True)
    #only accepting in year-month-date format rn 2006-10-25
    #Date formats needs to be defined DATE_INPUT_FORMATS = ['%m-%d-%Y'],ours is enforced through the dialog showup.
    dob = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ('username', 'email' ,'first_name', 'last_name', 'password1', 'password2','hadd','wadd','phone',)