from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.projects, name='projects'),
    # path('detail_tasks', views.detail_tasks, name='detail_tasks')
]
