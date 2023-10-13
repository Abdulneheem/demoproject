from django.contrib import admin
from django.urls import path,include

from books import views

app_name = 'books'

urlpatterns = [
    path('',views.home,name="home"),
    # path('addbooks/',views.addbooks,name="addbooks"),
    path('addbooks/viw/',views.viw,name="viw"),
    path('addbookss',views.addbookss,name="addbookss"),
    path('viewbooks/<int:p>',views.viewbook,name="viewbook"),
    path('delete/<int:p>',views.delete,name="delete"),
    path('editbook/<int:p>',views.editbook,name="editbook")
]