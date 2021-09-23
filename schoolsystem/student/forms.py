from django import forms
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields import IntegerField
from django.forms import TextInput, EmailInput
from django.forms.widgets import ClearableFileInput, DateInput, EmailInput, FileInput, NumberInput, Select, TextInput, SelectDateWidget
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"    #creating a form that contains attributes of all the models
        widgets = {
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px;',
                'placeholder': 'FirstName'
                }),

            'last_name':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px;',
                'placeholder': 'SecondName'
                }),

            'age':NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px;',
                'placeholder': 'Age'
                }),

            'email_address': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px;',
                'placeholder': 'Email'
                }),

            'phone_number':TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px;',
                'placeholder': 'PhoneNumber'
                }),

            'nationality':Select(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px;',
                'placeholder': 'Nationality'
                }),
            
             'medical_form':ClearableFileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px;',
                'placeholder': 'Allergies',
                'multiple':True,
                }),

            'academic_year':NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px;',
                'placeholder': 'Year joined'
                }),

             'admission_date':DateInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px;',
                'placeholder': 'academic_year'
                },
                format='%Y-%m-%d'
                ),
            
            'profile_pic':FileInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px;',
                'placeholder': 'Image',
                'multiple':True,
                }),

            'gender':Select(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px;',
                'placeholder': 'Gender',
                }),

            'date_of_birth':DateInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 500px;',
                'placeholder': 'date_of_birth',
                },
                format='%Y-%m-%d'
                ),           
        }

    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['academic_year'].input_formats = ('%Y-%m-%d',)
        self.fields['admission_date'].input_formats = ('%Y-%m-%d',)
        self.fields['date_of_birth'].input_formats = ('%Y-%m-%d',)

