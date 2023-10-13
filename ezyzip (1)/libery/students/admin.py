from django.contrib import admin

# Register your models here.

from students.models import StudentDetails

admin.site.register(StudentDetails)