from django.http import HttpResponse
from django.contrib import messages

# importing loading from django template
from django.template import loader
from django.shortcuts import render
from tasks.models import Task, SubTask
from datetime import datetime


def get_seconds_difference(before, after):
    print(before)
    print(after)
    return (before - after).total_seconds() <= 14400


# our view which is a function named index
def index(request):

    # using utc because it can be used globally
    tasks = Task.objects.all()
    task_alert = []
    for task in tasks:
        d1 = datetime.now()
        d2 = datetime(task.due_date.year, task.due_date.month, task.due_date.day, task.due_date.hour, task.due_date.minute, task.due_date.second)
        alert = get_seconds_difference(d1, d2)
        if alert:
            task_alert.append(task)

    return render(request, 'index.html', {'all_tasks': task_alert})

    # getting our template
    # template = loader.get_template('index.html')
    #
    # # rendering the template in HttpResponse
    # return HttpResponse(template.render())




