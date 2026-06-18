from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm


def employee_list(request):
    employees = Employee.objects.all()

    return render(
        request,
        'employees/list.html',
        {'employees': employees}
    )


def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request,
                  'employees/add_employee.html',
                  {'form': form}
                  )


def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/edit_employee.html', {'form': form})
