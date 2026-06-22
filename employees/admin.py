from django.contrib import admin
from .models import Attendance, Department, Employee

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Attendance)
