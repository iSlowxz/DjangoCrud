from django.shortcuts import render, redirect
from .models import Employee  # Assuming you have an Employee model

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'your_app/employee_list.html', {'employees': employees})

def employee_add(request):
    if request.method == 'POST':
        return redirect('employee_list')
    return render(request, 'your_app/employee_add.html') 