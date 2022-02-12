import random

from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.

# def home(request):
#     html = f'<h1>{request.method}: This is home.</h1>'
#     # could return --> return HttpResponseNotFound()
#     # which is the same as --> return HttpResponse(status=404)
#     return HttpResponse(
#         html,
#         status=202,
#         # content_type='text/plain',
#         headers={
#             'x-current-header': 'Django',
#         }
#     )
from employees_app.employees.models import Department, Employee


def validate_positive(value):
    if value < 0:
        raise ValidationError('value must be positive')


class EmployeeForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        label='Enter first name',
    )

    last_name = forms.CharField(
        max_length=40,
    )

    age = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            # attrs={'type': 'range'}
        ),
        validators=(
            validate_positive,
        )
    )


def home(request):
    return render(request, 'index.html')


# standard get/post view:
def create_employee(request):
    if request.method == 'GET':
        pass
        # get/show form
        context = {
            'employee_form': EmployeeForm(),
        }
        return render(request, 'employees/create.html', context)
    else:
        # save info
        employee_form = EmployeeForm(request.POST)
        if employee_form.is_valid():
            return redirect('index')
        pass
#
# def not_found(request):
#     return HttpResponseNotFound()
#     # or --> raise Http404()
#
#
# def go_to_home(request):
#     # return redirect(to='/') <--- hardcoded path
#     # return redirect(to='index')
#     # ^ path with named url (mapped path url to view)
#
#     return redirect('department details', id=random.randint(1, 9))
#
#
# def department_details(request, id):
#     if not isinstance(id, int):
#         pass
#
#     return HttpResponse(f'This is department {id}.')
#
#
# def create_department(request):
#     return HttpResponse('Created')
#
#
# def list_departments(request):
#     # create new department on refresh/entering page:
#     # OPTION 1
#     department = Department(
#         name=f'Department {random.randint(1, 999)}',
#     )
#     department.save()  # <---- saves to the DB, thus creating the object
#     # OPTION 2
#     Department.objects.create(
#         name=f'Department {random.randint(1, 999)}',
#     )  # <--- saves automatically
#
#     context = {
#         'departments': Department.objects.prefetch_related('employee_set').all(),
#         'employees': Employee.objects.all(),
#         # 'employees': Employee.objects.filter(first_name__exact='Thomas'),
#     }
#     return render(request, 'list_departments.html', context)
