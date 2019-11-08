from django.db import models
from django.forms import ModelForm


class Course(models.Model):
    Days = (
        (0, 'Saturday'),
        (1, 'Sunday'),
        (2, 'Monday'),
        (3, 'Tuesday'),
        (4, 'Wednesday'),
    )
    department = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    course_number = models.PositiveIntegerField()
    group_number = models.PositiveIntegerField()
    teacher = models.CharField(max_length=30)
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.IntegerField(choices=Days)
    second_day = models.IntegerField(choices=Days, blank=True, null=True)
    exam_date = models.DateField()

    def __str__(self):
        return self.name


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('department', 'name', 'course_number', 'group_number',
                  'teacher', 'start_time', 'end_time', 'first_day', 'second_day', 'exam_date')
