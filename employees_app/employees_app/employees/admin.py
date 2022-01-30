from django.contrib import admin

# Register your models here.
from employees_app.employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
