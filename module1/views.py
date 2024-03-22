from django.http import HttpResponse
from django.shortcuts import render

from .forms import PieChartForm, IntegerDateForm


# Create your views here.
def hello1(request):
    return HttpResponse("<center style=color:Blue;>Welcome to TTM homepage</center>")

def hello(request):
    return render(request,'hello.html')

def newhomepage(request):
    return render(request,'newhomepage.html')

def travelpackage(request):
    return render(request,'travelpackage.html')

def print1(request):
    return render(request,'print_to_console.html')
def print_to_console(request):
    if request.method=="POST":
        your_name = request.POST['your_name']
        print(f'your name:{your_name}')
   # return HttpResponse('Form Submitted Successfully')
    a1={'your_name':your_name}
    return render(request,'print_to_console.html',a1)
import random,string

def random2(request):
    return render(request,'random15.html')
def random15(request):
    if request.method == 'POST':
        input1=request.POST['input1']
        input2=int(input1)
        ran2=''.join(random.sample(string.digits,input2))
        print(ran2)
    a2={'ran2':ran2}
    return render(request,'random15.html',a2)

'''def getdate1(request):
    return render(request,'datetime123.html')


import datetime
from django.shortcuts import render
def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request,'get_date.html',{'updated_date':updated_date})
        else:
            form = IntegerDateForm()
        return render(request,'get_date.html',{'form':form})'''
def tzfunctioncall(request):
    return render(request,'pytzexample.html')

def pagecall(request):
    return render(request,'myregisterpage.html')

from .models import *
from django.shortcuts import render,redirect
def registerloginfunction(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        #check if the email already exists
        if Register.objects.filter(email=email).exists():
            message1 = "Email already registered. Choose a different email"
            #return HttpResponse("Email Already exists,choose another email")
            return render(request,'myregisterpage.html',{'message':message1})
        #create a new register instance and save it
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request,'myregisterpage.html')


import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})
def si(request):
    return render(request,'slides.html')

def getdate1(request):
    return render(request,'date.html')

import datetime
from django.shortcuts import render
def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']

            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request,'date.html',{'updated_date':updated_date})
        else:
            form = IntegerDateForm()
        return render(request,'date.html',{'form':form})


from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'newhomepage.html')
        else:
            messages.info(request,'Invalid crenditals')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def signup1(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['password']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Usename already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created Succesfully')
                return render(request,'login.html')
        else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return render(request,'newhomepage.html')
def feedback(request):
    return render(request,'contactus.html')

def contactmail(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        comment=request.POST['comment']
        tosend=comment +' ________________ this is just feedback form'
        data=contactus(firstname=firstname,lastname=lastname,email=email,comment=comment)
        data.save()
        return HttpResponse("<h1><center>Thank you for giving the feedback</center></h1>")

def weathercall(request):
    return render(request, 'weather_input.html')


import requests


def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '8d58d5a9d01f43e96a17ac1ce9c9f74f'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15, 2)
            return render(request, 'weather_input.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weather_input.html', {'error_message': error_message})