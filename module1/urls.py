
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("hello2/",hello1),
    path('hello/',hello,name='hello'),
    path('o/',newhomepage,name='newhomepage'),
    path('jash/',travelpackage,name='travelpackage'),
    path('jash1/',print_to_console,name='print_to_console'),
    path('p/', print1, name='print1'),
    path('p1/',random2,name='random2'),
    path('ran2/',random15,name='random15'),
    path('tzfunctioncall/',tzfunctioncall,name='tzfunctioncall'),
    path('Register/',pagecall,name='pagecall'),
    path('j/',registerloginfunction,name='registerloginfunction'),
    path('ls/',pie_chart,name='pie_chart'),
    path('ls1/',si,name='si'),
    path('wcall/', weathercall, name='weathercall'),
    path('wlogic/', weatherlogic, name='weatherlogic'),
    path('time/',getdate1,name='getdate1'),
    path('date/',get_date,name='get_date'),
    path('k/',login,name='login'),
    path('k1/',signup,name='signup'),
    path('k2/',login1,name='login1'),
    path('k3/',signup1,name='signup1'),
    path('k4/',logout,name='logout'),
    path('k6/', feedback, name='feedback'),
    path('contactmail/', contactmail, name='contactmail'),
]
