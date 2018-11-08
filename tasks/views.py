# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from tasks.models import Task
from .models import Task,SubTask
from datetime import datetime,timedelta

import pytz


def get_hours_difference(due_date):
    utc = pytz.UTC
    time_after = datetime.now().replace(tzinfo=utc) + timedelta(seconds=3600*4)
    time_before = datetime.now().replace(tzinfo=utc)
    print (time_after)
    print (time_before)
    due_date_in_utc = due_date.replace(tzinfo=utc)
    print (due_date_in_utc)
    if time_before <= due_date_in_utc:
        if due_date_in_utc <= time_after:
            return True
        else:
            return False
    else:
        return False


def update(request, tasks_id):

    task = Task.objects.get(id=tasks_id)
    if task.state:
        task.state = 0
    else:
        task.state = 1

    # print (task.id)
    task.save()

    for sub_tasks in task.sub_task_many.all():
        if task.state:
            sub_tasks.sub_state = 1
        else:
            sub_tasks.sub_state = 0
        sub_tasks.save()


    tasks = Task.objects.all()
    task_alert = []
    for task in tasks:
        alert = get_hours_difference(task.due_date)
        if alert:
            task_alert.append(task)

    return render(request, 'index.html', {'all_tasks': task_alert})


def sub_task_update(request, tasks_id):
    task_id = -1
    sub_task = SubTask.objects.get(id=tasks_id)
    if sub_task.sub_state:
        sub_task.sub_state = 0
    else:
        sub_task.sub_state = 1

    sub_task.save()

    tasks = Task.objects.all()
    task_alert = []

    for all_task in tasks:
        for sub_tasks in all_task.sub_task_many.all():
            global task_id
            print (sub_tasks.sub_title)
            print (sub_tasks.id)
            print (tasks_id)
            if str(sub_tasks.id) == str(tasks_id):
                print ("hello")
                task_id = all_task.id
                break
        if task_id != -1:
            break

    print (task_id)
    get_task = Task.objects.get(id=task_id)  # type: Task
    flag = False
    for all_sub_tasks in get_task.sub_task_many.all():
        global flag
        if all_sub_tasks.sub_state:
            flag = True
        else:
            flag = False
            break

    if flag:
        if get_task.state:
            get_task.state = 0
        else:
            get_task.state = 1
    else:
        if get_task.state:
            get_task.state = 0

    get_task.save()

    for task in tasks:
        alert = get_hours_difference(task.due_date)
        if alert:
            task_alert.append(task)

    return render(request, 'index.html', {'all_tasks': task_alert})

