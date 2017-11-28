# -*- coding: utf-8 -*-
from django.forms import ModelForm, Textarea, TextInput
from .models import Task

class NewTaskForm(ModelForm):
    """ Form to create new task. """
    
    class Meta:
        model = Task
        fields = ['task_title', 'description']
        widgets = {
            'task_title': TextInput(attrs={'class': 'form-control', 'id': 'new_task_title'}),
            'description': Textarea(attrs={'class': 'form-control', 'id': 'new_description'}),
        }
