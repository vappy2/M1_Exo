from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    todolist = Task.objects.order_by('created_date')
    output = '<br/>'.join([t.content for t in todolist])
    return HttpResponse(output)
