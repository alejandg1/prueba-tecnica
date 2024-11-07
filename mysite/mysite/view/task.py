from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Task

class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'task_list.html', {'tasks': tasks})

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'completed', 'category']
    template_name = 'task_create.html'
    success_url = reverse_lazy('task-list')


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed', 'category']
    template_name = 'task_update.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task-list')