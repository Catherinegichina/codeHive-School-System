from django.shortcuts import render

# Create your views here.
from datetime import date
from typing import Counter
from django.shortcuts import render
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses

# Create your views here.

def home(request):
    student=Student.objects.count()
    trainer=Trainer.objects.count()
    courses=Courses.objects.count()

    data = {"student": student, "trainer": trainer, "course": courses}
    return render(request, "home.html", data)



