from django.urls import path
from .views import TodoListView, TodoDetailView, TodoCreateView, TaskCreateView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-list'),
    path('create/', TodoCreateView.as_view(), name='todo-create'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('<int:pk>/task/add/', TaskCreateView.as_view(), name='task-create'),
]