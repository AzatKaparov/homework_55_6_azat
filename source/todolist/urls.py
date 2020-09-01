"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from accounts.views import login_view, logout_view
from webapp.views import TaskIndexView, TaskView, TaskCreateView, TaskDeleteView, TaskUpdateView,\
    ProjectIndexView, ProjectView, ProjectCreateView, ProjectTaskCreateView, ProjectDeleteView, \
    ProjectUpdateView

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskIndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='view'),
    path('task/add/', TaskCreateView.as_view(), name='create'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
    path('projects/', ProjectIndexView.as_view(), name='project_index'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/add', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/task/add/', ProjectTaskCreateView.as_view(), name='create_task_project'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),
]
