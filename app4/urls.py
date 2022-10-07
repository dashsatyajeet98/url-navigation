from django.urls import path
from app4.views import *
app_name='app4'

urlpatterns=[path('sthird/',sthird,name='sthird'),]