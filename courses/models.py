from django.db import models

# Create your models here.

class Courses(models.Model):
    course_profile_pic=models.ImageField(upload_to = 'images/')
    course_name=models.CharField(max_length=40)
    course_id=models.PositiveSmallIntegerField(null=True)
    course_description=models.CharField(max_length=200)
    course_trainer=models.CharField(max_length=40)
    course_room=models.CharField(max_length=10)
    course_email=models.EmailField(null=True)
    course_channel=models.CharField(max_length=20)
    course_calendar=models.DateField(null=True)
    course_syllabus=models.FileField(upload_to="documents/",null=True, blank=True)
    