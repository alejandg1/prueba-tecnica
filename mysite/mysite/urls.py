from django.urls import path
from .project import (
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
)
from .task import (
    TaskListView, 
    TaskCreateView, 
    TaskUpdateView, 
    TaskDeleteView
)


urlpatterns = [
    path('project/', ProjectListView.as_view(), name='project_list'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/edit/<int:pk>/', ProjectUpdateView.as_view(), name='project_edit'),
    path('project/delete/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/edit/<int:pk>/', TaskUpdateView.as_view(), name='task-edit'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]