"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/<int:project_id>/categories/', CategoryListView.as_view(), name='list_categories'),
    path('project/<int:project_id>/categories/create/', CategoryCreateView.as_view(), name='create_category'),
    path('project/<int:project_id>/categories/<int:category_id>/update/', CategoryUpdateView.as_view(), name='update_category'),
    path('project/<int:project_id>/categories/<int:category_id>/delete/', CategoryDeleteView.as_view(), name='delete_category'),
]
