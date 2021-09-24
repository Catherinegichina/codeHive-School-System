from django.db import models
from django.db.models.enums import Choices
from datetime import date
from django.db.models.fields.files import FileField, ImageField
# Create your models here.

class Student(models.Model):
    profile_pic=models.ImageField(upload_to = 'images/')
    first_name=models.CharField(max_length=12, null=True)
    last_name=models.CharField(max_length=12, null=True)
    gender_choice=(
        ('1','Female'),
        ('2','Male'),
        ('3','Prefer not to say')
    )
    gender=models.CharField(max_length=8,choices=gender_choice, null=True)
    age=models.PositiveSmallIntegerField(null=True)
    date_of_birth=models.DateField(null=True)
    phone_number=models.CharField(max_length=10)
    nationality_choice=(
        ('1','Rwandan'),
        ('2','Kenyan'),
        ('3','Ugandan'),
        ('4','SouthSudanes'),
        ('5','Sudanes')
    )
    nationality=models.CharField(max_length=15,choices=nationality_choice, null=True)
    national_Id=models.CharField(max_length=20)
    email_address=models.EmailField(null=True)
    admission_date=models.DateField(null=True, blank=True)
    medical_form=models.FileField(upload_to="documents/",null=True)
    laptop_serial_number=models.CharField(max_length=30, null=True, blank= True)
    academic_year=models.CharField(max_length=12)
    course_name=models.CharField(max_length=25, null=True, blank=True)



