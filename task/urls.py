# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'task'

urlpatterns = [
    # /task/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # Create new form.
    url(r'^newtaskform/$', views.NewTaskFormView.as_view(), name='newtaskform'),
    # Get table with all tasks.
    url(r'^tasklisttable/$', views.TaskListView.as_view(), name='tasklisttable'),
    # Toggle task done checkbox.
    url(r'^checktask/$', views.checkTask, name='checktask'),
]
