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


# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#         label='Enter first name',
#     )
# 
#     last_name = forms.CharField(
#         max_length=40,
#     )
# 
#     age = forms.IntegerField(
#         required=False,
#         widget=forms.TextInput(
#             # attrs={'type': 'range'}
#         ),
#         validators=(
#             validate_positive,
#         )
#     )

class EmployeeForm(forms.ModelForm):
    # age = forms.IntegerField(
    #     validators=(
    #         validate_positive,
    #     )
    # )
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bot_catcher(self):
        value = self.cleaned_data['bot_catcher']
        if value:
            raise ValidationError('This is a bot.')

    class Meta:
        model = Employee
        # fields = ('first_name', 'last_name', 'egn') or all of them:
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }


# this is how to disable EGN field editing while editing current user's info
# ------> when editing -> inherit the CREATE FORM (base creation of model) then edit stuff:
class EditEmployeeForm(EmployeeForm):
    # validating different fields:
    # def clean(self):
    #     pass

    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'egn': forms.TextInput(
                attrs={'readonly': 'readonly'},
            )
        }


class EmployeeOrderForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('first_name', 'First name'),
            ('last_name', 'Last name'),
        )
    )


def home(request):
    return render(request, 'index.html')


# standard get/post view:
# def create_employee(request):
#     if request.method == 'GET':
#         pass
#         # get/show form
#         context = {
#             'employee_form': EmployeeForm(),
#         }
#         return render(request, 'employees/create.html', context)
#     else:
#         # save info
#         employee_form = EmployeeForm(request.POST)
#         if employee_form.is_valid():
#             return redirect('index')
#
#         context = {
#             'employee_form': employee_form,
#         }
#         return render(request, 'employees/create.html', context)

# ^ optimized same view:
def create_employee(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST)
        if employee_form.is_valid():
            employee_form.save()  # saves to DB
            return redirect('index')

    else:
        employee_form = EmployeeForm()

    employee_order_form = EmployeeOrderForm(request.GET)
    employee_order_form.is_valid()
    order_by = employee_order_form.cleaned_data.get('order_by', 'first_name')

    context = {
        'employee_form': employee_form,
        'employees': Employee.objects.order_by(order_by).all(),
        'employee_order_form': employee_order_form,
    }

    return render(request, 'employees/create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == 'POST':
        employee_form = EditEmployeeForm(request.POST, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('create employee')
    else:
        employee_form = EditEmployeeForm(instance=employee)

    context = {
        'employee': employee,
        'employee_form': employee_form,
    }

    return render(request, 'edit.html', context)

# -----------------------------------
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
