from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project_detail/<int:id>', views.project_detail, name='project_detail'),
    path('project_detail/<int:id>/tasks_detail/<str:name>', views.task_detail, name='task_detail')
    # path('detail_tasks', views.detail_tasks, name='detail_tasks')
]
