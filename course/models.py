from django.db import models
from django.forms import ModelForm

class Course(models.Model):
    department = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    course_number = models.PositiveIntegerField()
    group_number = models.PositiveIntegerField()
    teacher = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    first_day = models.DateField()
    second_day = models.DateField(blank=True)

    def __str__(self):
        return self.name

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['department', 'name', 'course_number', 'group_number',
                  'teacher', 'start_time', 'end_time', 'first_day', 'second_day']
