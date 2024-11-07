# views.py
from django.shortcuts import render, redirect
from .forms import TaskForm  # Usa el formulario que necesitas
from .models import Task

def task_create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    context = {
        'form': form,
        'title': 'Create Task',
        'button_text': 'Save Task'
    }
    return render(request, 'form_template.html', context)
