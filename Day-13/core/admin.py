from django.contrib import admin
from .models import TodoList, Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    inlines = [TaskInline]
    list_display = ('title', 'user', 'created_at')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'todo_list', 'completed')