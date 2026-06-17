from django.shortcuts import redirect, render
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
