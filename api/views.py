
# Create your views here.
from django.shortcuts import render
from rest_framework import serializers, viewsets
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from events.models import Events

from .serializers import StudentSerializer
from .serializers import TrainerSerializer
from .serializers import CourseSerializer
from .serializers import EventSerializer
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    

class EventViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer