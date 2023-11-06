from typing import Any
from django.db import models
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        messages.success(self.request, 'The task was deleted successfully.')
        return super(TaskDelete,self).form_valid(form)
    
    def get_queryset(self):
        base_qs = super(TaskDelete, self).get_queryset()
        return base_qs.filter(user=self.request.user)



class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self,form):
        messages.success(self.request, 'The task was updated successfully')
        return super(TaskUpdate,self).form_valid(form)
    
    def get_queryset(self):
        base_qs = super(TaskUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self,form):
        form.instance.user = self.request.user
        messages.success(self.request, 'The task was created successfully')
        return super(TaskCreate,self).form_valid(form)


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    content_object_name = 'task'

    def get_queryset(self):
        base_qs= super(TaskDetail,self).get_queryset()
        return base_qs.filter(user=self.request.user)

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context

def home(request):
    return render(request, 'home.html')

