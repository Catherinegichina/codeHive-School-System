from django.shortcuts import render

# Create your views here.



from .models import Student
from django.shortcuts import redirect, render
from .models import Student


from django.shortcuts import render
from .forms import StudentRegistrationForm

def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print(f'You are now fully registered')
        else:
            print(form.errors)
    else:
        form = StudentRegistrationForm()
    return render(request, "register_student.html", {"form":form})

def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students":students})

def edit_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST, instance=Student)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = StudentRegistrationForm(instance=Student)     
    return render(request, "edit_student.html", {"form":form})       

def student_profile(request, id):
    student = Student.objects.get(id=id)
    return render(request, "student_profile.html", {"student":student})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("student_list")