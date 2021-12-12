from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Projects, Tasks

from Utils.decorator import login_required

    

@login_required
def projects(request):
    projects = Projects.objects.filter(user = request.user)
    tasks = Tasks.objects.filter(project__user = request.user)
    context = {
        'projects': projects,
        'tasks': tasks
    }
    return render(request, 'projects.html', context)

@login_required
def project_detail(request, id):
    
    try:
        project = Projects.objects.filter(user = request.user).get(id = id)
        tasks = Tasks.objects.filter(project__id = id).filter(project__user = request.user)
    except:
        return redirect('home:projects')
    
    context = {
        'project': project,
        'tasks': tasks
    }
    return render(request, 'project_detail.html', context)

def task_detail(request, id, name):
    
    try:
        project = Projects.objects.filter(user = request.user).get(id = id)
        tasks = Tasks.objects.filter(project__id = id).filter(project__user = request.user).get(name = name)
    except:
        return redirect('home:projects')
    
    context = {
        'project': project,
        'tasks': tasks
    }
    return HttpResponse(f'{tasks.name}')