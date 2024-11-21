from django.shortcuts import render, redirect, get_list_or_404
from django.urls import reverse_lazy
from .models import Stu_record, Course, Enrollment
from django.views.generic import ListView

# Create student views here.
class stuRecordView(ListView):
    model = Stu_record
    template_name = 'stu_record.html'
    context_object_name = 'student'


# Create course views here.
class courseListView(ListView):
    model = Course
    template_name = 'course.html'
    context_object_name = 'course'


# Create Enrollment views here.
class enrollmentListView(ListView):
    model = Enrollment
    template_name = 'enrollment.html'
    context_object_name = 'enrollment'



