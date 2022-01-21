from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django101.tasks.models import Task


def home(request):
    items = Task.objects.all()
    items_strings = [f'<li>{t.title}</li>' for t in items]
    items_string = ''.join(items_strings)
    html = f'''
    <h1>It works</h1>
    <ul>
    {items_string}
    </ul>
    '''
    return HttpResponse(html)


def profile(request):
    return HttpResponse("Profile info")


def profile_pic(request):
    return HttpResponse("Profile pic")
