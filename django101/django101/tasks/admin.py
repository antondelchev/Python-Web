from django.contrib import admin

# Register your models here.
from django101.tasks.models import Task


# option 1
# admin.site.register(Task)


# option 2

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
