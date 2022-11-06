from django.shortcuts import render, redirect
from .models import TodoList
from .forms import TodoForm
from django.http import HttpResponse

# Create your views here.

def home(request):

    tasks = TodoList.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
        
    return render(request, 'home.html', {'tasks': tasks, 'form': form})


def update_tast(request, id):

    task = TodoList.objects.get(id=id)
    form = TodoForm(instance=task)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'update.html', {'task': task, 'form': form})

def delete_tast(request, id):
    
    task = TodoList.objects.get(id=id)
    task.delete()

    return redirect('/')




