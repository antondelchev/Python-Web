from django.contrib import admin

from todos_app.todos.models import Todo, Person, Category


class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'text',
        'owner',
    ]
    sortable_by = ['text']
    list_filter = ['owner']

    def has_change_permission(self, request, obj=None):
        return True


admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
admin.site.register(Category)
