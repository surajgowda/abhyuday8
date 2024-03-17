from django.shortcuts import render
from .models import Task, TeamDetails, Objectives

def team_details_view(request):
    tasks = Task.objects.all()  # Fetch all tasks
    departments = set(task.dept.department for task in tasks)
    team_details = TeamDetails.objects.all()
    return render(request, 'team_details.html', {'team_details': team_details,'departments': departments, 'tasks': tasks})

def department_tasks(request, department_id):
    tasks = Task.objects.filter(dept__id=department_id).order_by('deadline')

    # Pass tasks to the template
    return render(request, 'department_tasks.html', {'tasks': tasks})

def home(request):
    tasks = TeamDetails.objects.all()  # Fetch all tasks
    departments_with_objectives = []
    objectives = Objectives.objects.all()
    for objective in objectives:
        lines = objective.objectives_list.split('\n')
        departments_with_objectives.append({'team': objective.team_name.department, 'objectives': lines})
    departments_with_objectives.append({'task':tasks})
    return render(request, 'index.html', {'departments_with_objectives': departments_with_objectives, 'tasks': tasks})

def nav(request):
    tasks = Task.objects.all()  # Fetch all tasks
    departments = set(task.dept.department for task in tasks)  # Extract unique department names
    return render(request, 'navbar.html', {'departments': departments, 'tasks': tasks})

