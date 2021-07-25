from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView ,ListView, UpdateView, DeleteView, DetailView
from .models import Todolist
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CreateTask(LoginRequiredMixin,CreateView):
    model = Todolist
    fields = ['title','description','complete']
    template_name = "Todolist/create_task.html"
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)

class Taskdetail(LoginRequiredMixin, DetailView):
    model = Todolist
    context_object_name = 'task'
    template_name = "Todolist/tasks_detail.html"

class Taskslist(LoginRequiredMixin, ListView):
    model = Todolist
    context_object_name = 'tasks'
    template_name = "Todolist/tasks_list.html"

    #Only the creator can see the tasks
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Todolist
    fields = ['title','description','complete']
    template_name = "Todolist/update_task.html"
    success_url = reverse_lazy('tasks')

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Todolist
    template_name = "Todolist/delete_task.html" 
    success_url = reverse_lazy('tasks')