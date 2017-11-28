# -*- coding: utf-8 -*-
from django.views import generic
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateResponseMixin, View
from django.http import HttpResponse
from django.utils import timezone

from .models import Task
from .forms import NewTaskForm
from operator import attrgetter

class TaskListView(generic.ListView):
    """ Table of all tasks. """

    template_name = 'task/tasklist.html'
    context_object_name = 'all_tasks'

    def get_queryset(self):
        return sorted(Task.objects.all(), key=attrgetter('date'), reverse=True)

class NewTaskFormView(FormView):
    """ Form to create new task. """

    template_name = 'task/newtaskform.html'
    form_class = NewTaskForm
    success_url = '/task/tasklisttable/'

    def form_valid(self, form):
        title = form["task_title"].data
        des = form["description"].data
        t = Task(task_title=title, description=des, date=timezone.now())
        t.save()
        return super(FormView, self).form_valid(form)

class IndexView(TemplateResponseMixin, View):
    """ Index page. """

    template_name = 'task/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        for cview in [NewTaskFormView, TaskListView]:
            clsview = cview.as_view()
            view = clsview(request, *args, **kwargs)
            context.update(view.context_data)
        return self.render_to_response(context)

def checkTask(request):
    """ Mark task solved/unsolved. """

    task_solved = request.POST.get('taskcheck') == 'on'
    t = Task.objects.get(pk=request.POST['taskid'])
    t.is_solved = task_solved
    t.save()
    return HttpResponse()
