from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employee
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer


@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)

        return JsonResponse(departments_serializer.data, safe=False)



    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)

        if departments_serializer.is_valid():
            departments_serializer.save()

            return JsonResponse('Department saved!', safe=False)
        return JsonResponse('Failed to save')

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentsId=department_data['DepartmentsId'])
        departments_serializer = DepartmentSerializer(department, data = department_data)

        if departments_serializer.is_valid():
            departments_serializer.save()

            return JsonResponse('Update successfull', safe=False)

        return JsonResponse('Failed to Update!', safe =False)


    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentsId=id)
        department.delete()

        return JsonResponse('Delete successfull', safe=False)






@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employee = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employee, many=True)

        return JsonResponse(employee_serializer.data, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)

        if employee_serializer.is_valid():
            employee_serializer.save()

            return JsonResponse('Employee saved!', safe=False)
        return JsonResponse('Failed to save', safe=False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee, data = employee_data)

        if employee_serializer.is_valid():
            employee_serializer.save()

            return JsonResponse('Update successfull', safe=False)

        return JsonResponse('Failed to Update!', safe =False)


    elif request.method == 'DELETE':
        employee = Employee.objects.get(EmployeeId=id)
        employee.delete()

        return JsonResponse('Delete successfull', safe=False)