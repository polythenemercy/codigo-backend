from django.shortcuts import render
from django.views.generic import ListView
from app.models import Task

# Create your views here.
def task_list(request):
  tasks = Task.objects.all()
  return render(request, 'task_list.html', {'task': tasks})

#Generic class based views
class TaskListView(ListView):
  context_object_name = 'tasks'
  queryset = Task.objects.all()
  template_name = 'task_list.html'
