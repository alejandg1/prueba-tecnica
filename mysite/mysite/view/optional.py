from django.views.generic import TemplateView
from ..models import Project, Category, Task

class ProjectSummaryView(TemplateView):
    template_name = 'summary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all()
        summary_data = []

        for project in projects:
            categories_count = Category.objects.filter(project=project).count()
            tasks_count = Task.objects.filter(category__project=project).count()
            completed_tasks_count = Task.objects.filter(
                category__project=project, completed=True
            ).count()

            summary_data.append({
                'project': project,
                'categories_count': categories_count,
                'tasks_count': tasks_count,
                'completed_tasks_count': completed_tasks_count,
            })

        context['summary_data'] = summary_data
        return context
