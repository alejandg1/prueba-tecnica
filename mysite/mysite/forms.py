from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['nombre']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'category']

class ProyectForm(forms.ModelForm):
    class Meta:
        model = Proyect
        fields = ['nombre', 'description']