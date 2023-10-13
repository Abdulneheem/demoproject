from django.contrib import admin
from django.urls import path,include

from photo import views

app_name = 'photo'

urlpatterns = [
    path('cr7/',views.cr7,name="cr7"),
    path('cr7/messi2/',views.messi,name="messi")
]