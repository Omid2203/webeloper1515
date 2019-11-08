from django.shortcuts import render
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



@login_required
def courses(request):
    form = CourseForm()
    if request.method=="POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'courses.html', {'form':form})