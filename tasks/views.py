# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Task,SubTask
from datetime import datetime


def get_seconds_difference(before, after):
    return abs(before - after).total_seconds() <= 14400


def update(request, tasks_id):

    task = Task.objects.get(id=tasks_id)
    if task.state:
        task.state = 0
    else:
        task.state = 1

    # print (task.id)
    task.save()

    tasks = Task.objects.all()
    task_alert = []
    for task in tasks:
        d1 = datetime.now()
        d2 = datetime(task.due_date.year, task.due_date.month, task.due_date.day, task.due_date.hour,
                      task.due_date.minute, task.due_date.second)
        alert = get_seconds_difference(d1, d2)
        if alert:
            task_alert.append(task)

    return render(request, 'index.html', {'all_tasks': task_alert})


def sub_task_update(request, tasks_id):
    sub_task = SubTask.objects.get(id=tasks_id)
    if sub_task.sub_state:
        sub_task.sub_state = 0
    else:
        sub_task.sub_state = 1

    sub_task.save()

    tasks = Task.objects.all()
    task_alert = []
    for task in tasks:
        all_sub_tasks = task.sub_task_many.all()
        flag = False
        for subTask in all_sub_tasks:
            # print (subTask.id)
            if subTask.sub_state:
                flag = True
            else:
                flag = False
                break

        if flag:
            # print (task.id)
            return update(request, task.id)

        d1 = datetime.now()
        d2 = datetime(task.due_date.year, task.due_date.month, task.due_date.day, task.due_date.hour,
                      task.due_date.minute, task.due_date.second)
        alert = get_seconds_difference(d1, d2)
        if alert:
            task_alert.append(task)

    return render(request, 'index.html', {'all_tasks': task_alert})

