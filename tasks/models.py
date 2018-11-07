# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime


# Create your models here.

class SubTask(models.Model):
    # task = models.ForeignKey(Task, on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=100)
    sub_description = models.CharField(max_length=100)
    sub_due_date = models.DateTimeField(default=datetime.now)
    sub_state = models.IntegerField(default=0)

    def __str__(self):
        return self.sub_title


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    due_date = models.DateTimeField(default=datetime.now)
    state = models.IntegerField(default=0)
    # sub_tasks = models.ForeignKey(SubTask, on_delete=models.CASCADE, related_name='sub_tasks')
    sub_task_many = models.ManyToManyField(SubTask,related_name='sub_tasks', null=True, blank=True)

    def __str__(self):
        return self.title





