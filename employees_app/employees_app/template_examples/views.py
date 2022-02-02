from django.shortcuts import render

# Create your views here.
from employees_app.employees.models import Employee


def index(request):
    context = {
        'title': 'THE Employees list',
        'employees': Employee.objects.order_by('first_name',).all(),
        'num_1': 123,
        'num_2': 300,
        'nums': [1, 2, 3, 4],
    }
    return render(request, 'templates_examples/index.html', context)
