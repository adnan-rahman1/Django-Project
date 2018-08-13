from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todos
from .forms import TodoModelForm


def showTodos(request):
    form = TodoModelForm()
    task_name = Todos.objects.all()
    context = { 'todos': task_name, 'form': form }
    return render(request, 'todo_app/index.html', context)


def addTodos(request):
    form = TodoModelForm()
    if (request.method == 'POST'):
        form = TodoModelForm(request.POST)
        if (form.is_valid()):
            form_data = form.save()
            form = TodoModelForm()
        return redirect('showTodos')

def completeTodos(request, task_id):
    todos = Todos.objects.get(pk=task_id)
    todos.complete = True
    todos.save()
    return redirect('showTodos')

def deleteTodos(request):
    todos = Todos.objects.filter(complete__exact=True)
    todos.delete()
    return redirect('showTodos')

def deleteAllTodos(request):
    todos = Todos.objects.all()
    todos.delete()
    return redirect('showTodos')
