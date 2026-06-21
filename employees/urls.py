from django.urls import path
from .views import attendance_list, dashboard, delete_employee, edit_employee, employee_add, employee_list

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('add/', employee_add, name='employee_add'),
    path('edit/<int:id>', edit_employee, name='edit_employee'),
    path('delete/<int:id>', delete_employee, name='delete_employee'),
    path('dashboard/', dashboard, name='dashboard'),
    path('attendance/', attendance_list, name='attendance_list'),
]
