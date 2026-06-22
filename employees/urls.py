from django.urls import path
from .views import add_attendance, attendance_list, dashboard, delete_attendance, delete_employee, edit_attendance, edit_employee, employee_add, employee_list

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('add/', employee_add, name='employee_add'),
    path('edit/<int:id>', edit_employee, name='edit_employee'),
    path('delete/<int:id>', delete_employee, name='delete_employee'),
    path('dashboard/', dashboard, name='dashboard'),
    path('attendance/', attendance_list, name='attendance_list'),
    path('attendance/add/', add_attendance, name='add_attendance'),
    path('attendance/edit/<int:id>/', edit_attendance, name='edit_attendance'),
    path('attendance/delete/<int:id>/',
         delete_attendance, name='delete_attendance'),

]
