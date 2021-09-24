from django import forms
from django.forms.widgets import DateInput, TextInput
from.models import Events
from django.forms import fields

class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model =Events
        fields="__all__"
        widgets = {
      'start_time': DateInput(attrs=
      {
        'type': 'datetime-local',
        'style': 'max-width: 300px;',
        'class': "form-control",
      }, 

      format='%Y-%m-%dT%H:%M'),

      'end_time': DateInput(attrs=
      {
        'type': 'datetime-local',
        'style': 'max-width: 300px;',
        'class': "form-control",    
      },
       
      format='%Y-%m-%dT%H:%M'),

      'event_name':TextInput(attrs=
      {
        'class': "form-control",
        'style': 'max-width: 300px;',
        'placeholder': 'Name'
      }),

      'event_location':TextInput(attrs=
      {
        'class': "form-control",
        'style': 'max-width: 300px;',
        'placeholder': 'Event Venue'
      }),     
    }

    def __init__(self, *args, **kwargs):
        super(EventRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)