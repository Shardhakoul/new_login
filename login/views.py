#users/views.py

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request,"login/home.html")
    '''if request.method == "POST":
        #validated form
        form_class = SignUpForm(request.POST)
        if form.is_valid():
            #save to db
            form.save()
            #log them in
            redirect("login/home.html")
    else:
        form = SignUpForm()
    return render(request,"login/signup.html",{'form':form})'''





class SignUp(CreateView):
    #Added feild and modified UserCreationForm for min login/forms.py
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "login/signup.html"

