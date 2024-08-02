from django.db import models

# Create your models here.
# scheduler_app/models.py

# scheduler_app/models.py
"""
from django.db import models

class ScheduledPost(models.Model):
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.text or 'No text'

# scheduler_app/models.py

from django.db import models

class ScheduledPost(models.Model):
    text = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.text
""" 

from django.db import models

class ScheduledPost(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='uploads/')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.text




