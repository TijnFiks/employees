from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Employee, Department
# Create your views here.

def index(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    return render(
        request,
        'index.html',
        {
            'employees': employees,
            'departments': departments
        }
    )

def new_employee(request):
    
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    department_id = int(request.POST['department_id'])
    id = int(request.POST['id'])
    employee = Employee(id=id, first_name=first_name, last_name=last_name, department_id=department_id)
    employee.save()
    return redirect(index)