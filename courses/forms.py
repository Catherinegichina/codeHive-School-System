from django import forms
from django.forms.widgets import EmailInput, FileInput, TextInput
from.models import Courses
from django.forms import fields

class CoursesRegistrationForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = "__all__"
        widgets = {
            'course_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'Course'
                }),

            'course_id':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px;',
                'placeholder': 'Id'
                }),

            'course_trainer':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px;',
                'placeholder': 'Trainer'
                }),

            'course_description':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px;',
                'placeholder': 'Description'
                }),

            'course_email':EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px;',
                'placeholder': 'Email'
                }),

            'course_profile_pic':FileInput(attrs={
            'class': "form-control", 
            'style': 'max-width: 500px;',
            'placeholder': 'Image',
            'multiple':True,
            }),
        }