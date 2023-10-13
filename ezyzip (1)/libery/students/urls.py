from django.contrib import admin
from django.urls import path,include

from students import views

app_name = 'students'

urlpatterns = [
    path('user_login',views.user_login,name="user_login"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('register',views.register,name="register"),
    path('studentdetails',views.studentDetails,name="studentdetails"),
    path('addstudentDetails',views.addstudentDetails,name="addstudentDetails"),
    path('factorial', views.factorial, name="factorial")
]

