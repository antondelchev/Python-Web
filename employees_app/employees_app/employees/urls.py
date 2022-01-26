from django.urls import path

from employees_app.employees.views import department_details, list_departments, not_found

urlpatterns = [
    path('<int:id>/', department_details),
    path('', list_departments),
    path('not-found/', not_found),
]
