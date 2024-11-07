from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Project, Category
from .forms import CategoryForm

class CategoryListView(ListView):
    model = Category
    template_name = 'mysite/list_categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        self.project = get_object_or_404(Project, id=self.kwargs['project_id'])
        return Category.objects.filter(project=self.project)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context



class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'mysite/category.html'

    def form_valid(self, form):
        project = get_object_or_404(Project, id=self.kwargs['project_id'])
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('list_categories', kwargs={'project_id': self.kwargs['project_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, id=self.kwargs['project_id'])
        return context


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'mysite/update_category.html'

    def get_object(self, queryset=None):
        project = get_object_or_404(Project, id=self.kwargs['project_id'])
        return get_object_or_404(Category, id=self.kwargs['category_id'], project=project)

    def get_success_url(self):
        return reverse_lazy('list_categories', kwargs={'project_id': self.kwargs['project_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, id=self.kwargs['project_id'])
        return context


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'mysite/delete_category.html'

    def get_object(self, queryset=None):
        project = get_object_or_404(Project, id=self.kwargs['project_id'])
        return get_object_or_404(Category, id=self.kwargs['category_id'], project=project)

    def get_success_url(self):
        return reverse_lazy('list_categories', kwargs={'project_id': self.kwargs['project_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, id=self.kwargs['project_id'])
        return context
