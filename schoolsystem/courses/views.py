from django.shortcuts import render

# Create your views here.
from .models import Courses
from django.shortcuts import redirect, render
from .forms import CoursesRegistrationForm

# Create your views here.

def register_courses(request):
    if request.method=="POST":
        form = CoursesRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_courses')
        else:
            print(form.errors)
    else:
        form = CoursesRegistrationForm()

    return render(request, "register_courses.html", {"form":form})

def course_list(request):
    courses = Courses.objects.all()
    return render(request, "course_list.html", {"courses":courses})

def edit_course(request, id):
    course = Courses.objects.get(id=id)
    if request.method == "POST":
        form = CoursesRegistrationForm(request.POST, instance=Courses)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = CoursesRegistrationForm(instance=Courses)     
    return render(request, "edit_course.html", {"form":form})       

def course_profile(request, id):
    course = Courses.objects.get(id=id)
    return render(request, "course_profile.html", {"course":course})

def delete_course(request, id):
    course = Courses.objects.get(id=id)
    course.delete()
    return redirect("course_list")
    