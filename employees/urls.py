from django.urls import path
from .views import employee_add, employee_list

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('add/', employee_add, name='employee_add')
]
