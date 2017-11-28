# -*- coding: utf-8 -*-
from django.db import models

class Task(models.Model):
    """ Task database row. """
    
    task_title = models.CharField(max_length=50)

    description = models.CharField(max_length=250)
    # Indicate whether task checkbox is checked.
    is_solved = models.BooleanField(default=False)
    # Creation date.
    date = models.DateTimeField()
