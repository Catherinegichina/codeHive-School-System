from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields.files import FileField

# Create your models here.

class Trainer(models.Model):
    profile_pic = models.ImageField(upload_to = 'images/')
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    gender_choice=(
        ('1','Female'),
        ('2','Male'),
        ('3','Prefer not to say')
    )
    gender=models.CharField(max_length=8,choices=gender_choice)
    age=models.PositiveSmallIntegerField(null=True, blank=True)
    date_of_birth=models.DateField(null=True)
    phone_number=models.CharField(max_length=10)
    nationality_choice=(
        ('1','Rwandan'),
        ('2','Kenyan'),
        ('3','Ugandan'),
        ('4','SouthSudanes'),
        ('5','Sudanes')
    )
    nationality=models.CharField(max_length=15,choices=nationality_choice)
    national_Id=models.CharField(max_length=20)
    email_address=models.EmailField(null=True)
    joining_date=models.DateField(null=True)
    resume=models.FileField(upload_to="documents/",null=True)
    contract=models.FileField(upload_to="documents/",null=True, blank=True)
    course_name=models.CharField(max_length=25)
    salary=models.PositiveBigIntegerField(null=True, blank=True)
    job_title=models.CharField(max_length=25)
    company=models.CharField(max_length=30)

def __str__(self):
    return self.first_name
