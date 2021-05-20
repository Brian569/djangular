from django.urls import path,re_path
from EmployeeApp.views import(
    departmentApi, employeeApi
)

urlpatterns = [
    path('department/', departmentApi),
    re_path(r'department/([0-9]+)', departmentApi),
    path('employee/', employeeApi),
    re_path(r'employee/([0-9]+)', employeeApi)

]