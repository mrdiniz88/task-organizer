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
