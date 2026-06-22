from django.shortcuts import render, get_object_or_404, redirect
from .models import Attendance, Department, Employee
from .forms import EmployeeForm, AttendanceForm
from django.contrib.auth.decorators import login_required


@login_required
def employee_list(request):
    employees = Employee.objects.all()

    return render(
        request,
        'employees/list.html',
        {'employees': employees}
    )


@login_required
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


@login_required
def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/edit_employee.html', {'form': form})


@login_required
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')

    return render(
        request,
        'employees/delete_employee.html',
        {'employee': employee}
    )


@login_required
def dashboard(request):
    employee_count = Employee.objects.count()
    department_count = Department.objects.count()
    context = {
        'employee_count': employee_count,
        'department_count': department_count
    }

    return render(request, 'employees/dashboard.html', context)


def attendance_list(request):

    attendance_records = Attendance.objects.all()

    return render(
        request,
        'employees/attendance_list.html',
        {'attendance_records': attendance_records}
    )


def add_attendance(request):

    if request.method == 'POST':

        form = AttendanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('attendance_list')

    else:
        form = AttendanceForm()

    return render(
        request,
        'employees/add_attendance.html',
        {'form': form}
    )


def edit_attendance(request, id):

    attendance = get_object_or_404(
        Attendance,
        id=id
    )

    if request.method == 'POST':

        form = AttendanceForm(
            request.POST,
            instance=attendance
        )

        if form.is_valid():
            form.save()
            return redirect('attendance_list')

    else:
        form = AttendanceForm(instance=attendance)

    return render(
        request,
        'employees/edit_attendance.html',
        {'form': form}
    )


def delete_attendance(request, id):

    attendance = get_object_or_404(
        Attendance,
        id=id
    )

    if request.method == 'POST':
        attendance.delete()
        return redirect('attendance_list')

    return render(
        request,
        'employees/delete_attendance.html',
        {'attendance': attendance}
    )
