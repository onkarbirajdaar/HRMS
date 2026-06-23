from django import forms
from .models import Employee, Leave, Attendance


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'status']


class LeaveForm(forms.ModelForm):

    class Meta:
        model = Leave
        fields = [
            'employee',
            'leave_type',
            'start_date',
            'end_date',
            'reason'
        ]
