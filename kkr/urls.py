from django.urls import path
from kkr.views import *

app_name='kkr'

urlpatterns=[
    path('venkatesh/', venkatesh, name='venkatesh'),
]