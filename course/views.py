from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import CourseForm, Course
from django.views.generic import ListView, CreateView

# Create your views here.
class CourseListView(ListView):
    template_name = 'courselist.html'
    model = Course
    context_object_name = 'course'

    def get_queryset(self):
        try:
            name = self.kwargs['department']
        except:
            name = ''
        if (name != ''):
            object_list = self.model.objects.filter(name__icontains = name)
        else:
            object_list = self.model.objects.all()
        return object_list

@login_required
def course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courselist.html', {'form': form})

    form = CourseForm()
    return render(request, 'courses.html', {'form': form})


@login_required
def courses(request):
    form = CourseForm()
    if request.method=="POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'courses.html', {'form':form,})