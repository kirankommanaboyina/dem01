from . import views
from django.urls import path
urlpatterns=[
    path('mail/',views.send_emails,name='send_emails'),  #if you want to execute the mail means you have to remove the mail/
]