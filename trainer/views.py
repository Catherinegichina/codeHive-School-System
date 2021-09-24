from django.shortcuts import render

# Create your views here.
from .models import Trainer
from django.shortcuts import redirect, render
from.forms import TrainerRegistrationForm
# Create your views here.

def register_trainer(request):
    if request.method == "POST":
        form = TrainerRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print(f'Welcome! You are now a member')
        else:
            print(form.errors)
    else:
        form = TrainerRegistrationForm()
    return render(request, "register_trainer.html",{"form":form})

def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, "trainer_list.htm", {"trainers":trainers})


def edit_trainer(request, id):
    trainer = Trainer.objects.get(id=id)
    if request.method == "POST":
        form = TrainerRegistrationForm(request.POST, instance=Trainer)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = TrainerRegistrationForm(instance=Trainer)
    return render(request, "edit_trainer.htm", {"form":form})

def trainer_profile(request, id):
    trainer = Trainer.objects.get(id=id)
    return render(request, "trainer_profile.htm", {"trainer":trainer})

def delete_trainer(request, id):
    trainer = Trainer.objects.get(id=id)
    trainer.delete()
    return redirect("trainer_list")
