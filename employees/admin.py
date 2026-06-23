from django.contrib import admin
from .models import Attendance, Department, Employee, Leave

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Attendance)
admin.site.register(Leave)
