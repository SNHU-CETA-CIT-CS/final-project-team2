from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method =='POST':    # now making the task save to the database
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/tasks/')  # go back to the template


    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect ('/tasks/')


    context = {'form':form}

    return render(request, 'taskupdate.html', context)

def deleteTask(request, pk):
    item= Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/tasks/')

    context = {'item':item}
    return render(request, 'deletetask.html', context)