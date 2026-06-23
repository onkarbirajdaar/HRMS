from django.urls import path
from .views import add_attendance, add_leave, attendance_list, dashboard, delete_attendance, delete_employee, edit_attendance, edit_employee, edit_leave, employee_add, employee_list, leave_list

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
    path('leave/', leave_list, name='leave_list'),
    path('leave/add/', add_leave, name='add_leave'),
    path('leave/edit/<int:id>/', edit_leave, name='edit_leave'),
]
