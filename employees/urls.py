from django.urls import path
from .views import edit_employee, employee_add, employee_list

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('add/', employee_add, name='employee_add'),
    path('edit/<int:id>', edit_employee, name='edit_employee')
]
