# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Task, SubTask

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    model = Task
    filter_horizontal = ('sub_task_many',)


admin.site.register(Task,TaskAdmin)
admin.site.register(SubTask)

