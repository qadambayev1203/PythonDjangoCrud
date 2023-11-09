from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return HttpResponse("Hello World")


class IndexClass(ListView):
    model=Student
    template_name='index.html'
    context_object_name='students'

class DetailClass(DetailView):
    model=Student
    template_name='detail.html'
    context_object_name='student'

class CreateClass(CreateView):
    model=Student
    template_name='create.html'
    fields=['name', 'sname', 'Email' ,'phone']

class UpdateClass(UpdateView):
    model=Student
    template_name='update.html'
    fields=['name', 'sname', 'Email' ,'phone']

class DeleteClass(DeleteView):
    model=Student
    template_name='delete.html'
    success_url=reverse_lazy('index')
