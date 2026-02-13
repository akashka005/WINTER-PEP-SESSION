from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import TodoList, Task


class TodoListView(LoginRequiredMixin, ListView):
    model = TodoList
    template_name = "todo/list_list.html"

    def get_queryset(self):
        return TodoList.objects.filter(user=self.request.user)


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = TodoList
    template_name = "todo/list_detail.html"


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = TodoList
    fields = ['title']
    template_name = "todo/list_form.html"
    success_url = reverse_lazy('todo-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title']
    template_name = "todo/task_form.html"

    def form_valid(self, form):
        form.instance.todo_list_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('todo-detail', kwargs={'pk': self.kwargs['pk']})