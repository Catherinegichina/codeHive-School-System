from django.db import models

# Create your models here.

from django.conf.urls import url
import datetime
from django.urls import reverse

# Create your models here.
class Events(models.Model):
    event_name=models.CharField(max_length=12)
    event_location=models.CharField(max_length=10)
    start_time = models.DateTimeField(default=datetime.date.today)
    end_time = models.DateTimeField(default=datetime.date.today)

def __str__(self):
    return self.event_name

@property
def get_htm_url(self):
    url = reverse('event_edit', args=(self.id,))
    return f'<p>{self.event_name}</p><a href="{url}">edit</a>'