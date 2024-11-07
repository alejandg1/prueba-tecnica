from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Project

class ProjectListView(ListView):
    model = Project
    template_name = 'project.html'
    context_object_name = 'projects'

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('project_list')

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_delete.html'
    success_url = reverse_lazy('project_list')
