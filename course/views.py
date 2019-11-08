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

class CourseCreateView(CreateView):
    template_name = 'courses.html'
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('courselist')

def course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            department = form.cleaned_data.get('department')
            name = form.cleaned_data.get('name')
            course_number = form.cleaned_data.get('course_number')
            group_number = form.cleaned_data.get('group_number')
            teacher = form.cleaned_data.get('teacher')
            start_time = form.cleaned_data.get('start_time')
            end_time = form.cleaned_data.get('end_time')
            first_day = form.cleaned_data.get('first_day')
            second_day = form.cleaned_data.get('second_day')

            form.save()
            return redirect('courselist')
    form = CourseForm()
    return render(request, 'courses.html', {'form': form})


@login_required
def courses(request):
    form = CourseForm()
    if request.method=="POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'courses.html', {'form':form})