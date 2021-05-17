from . import models
from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request,'index.html')

def privacy(request):
    return render(request, 'pages/privacy.html')

def service(request):
    return render(request, 'pages/service.html')

def work(request):
    return render(request, 'pages/work.html')
def about(request):
    return render(request, 'pages/about.html')

def register(request):


    if request.method == 'POST':

        user_form = forms.CustomerForm(request.POST)
     
        if user_form.is_valid():
            user = user_form.save()
        else:
            print(user_form.errors)

    else:

        user_form = forms.CustomerForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'pages/getintouch.html',
                          {'user_form':user_form})