from random import randrange

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django101.tasks.models import Task


# def home(request):
#     items = Task.objects.all()
#     items_strings = [f'<li>{t.title}</li>' for t in items]
#     items_string = ''.join(items_strings)
#     html = f'''
#     <h1>It works</h1>
#     <ul>
#     {items_string}
#     </ul>
#     '''
#     return HttpResponse(html)

def home(request):
    context = {
        'title': 'It works from view!',
        'tasks': Task.objects.all(),
        # 'tasks': [],
    }
    return render(request, 'home.html', context)


def profile(request):
    return HttpResponse("Profile info")


def profile_pic(request):
    return HttpResponse("Profile pic")


def progress(request):
    context = {
        'title': 'Percentage completion for each task:',
        'tasks': Task.objects.all(),
        'tasks_completion_and_names': [],
    }

    random_percents = [f'Completed: {randrange(100)}%' for _ in range(len(context['tasks']))]
    all_tasks_names = [f'Task name: {item.text} || ' for item in context['tasks']]
    context['tasks_completion_and_names'] = zip(all_tasks_names, random_percents)

    return render(request, 'progress.html', context)
