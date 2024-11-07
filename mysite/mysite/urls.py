from django.urls import path
from .views import (
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
)

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('create/', ProjectCreateView.as_view(), name='project_create'),
    path('edit/<int:pk>/', ProjectUpdateView.as_view(), name='project_edit'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
]