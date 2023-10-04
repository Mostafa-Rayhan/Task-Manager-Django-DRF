from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'task_list.html', {'tasks': tasks})

class TaskCreateView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'task_create.html', {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, 'task_create.html', {'form': form})

class TaskDetailView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'task_detail.html', {'tasks': tasks})
    
class TaskUpdateView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'task_update.html', {'tasks': tasks})
    
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, 'task_update.html', {'form': form, 'task': task})
    
class TaskDeleteView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'task_delete.html', {'tasks': tasks})
    
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('task_list')