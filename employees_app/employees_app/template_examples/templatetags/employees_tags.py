from django import template

from employees_app.employees.models import Employee

register = template.Library()


@register.inclusion_tag('tags/employees_list.html')
def employees_list():
    employees = Employee.objects.all()

    # context
    return {
        'employees': employees
    }
