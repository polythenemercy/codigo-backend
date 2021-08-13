from django.shortcuts import render
from django.views.generic import ListView
from app.models import Task

# Create your views here.
def task_list(request):
  tasks = Task.objects.all()
  return render(request, 'app/task_list.html', {'object_list': tasks})

#Generic class based views
class TaskListView(ListView):
  context_object_name = 'object_list'
  queryset = Task.objects.all()
  template_name = 'app/task_list.html'

class TaskModelListView(ListView):
  model = Task
