from tastypie.resources import ModelResource, fields
from tastypie.constants import ALL
from datetime import datetime, date,timedelta
from tastypie.exceptions import HttpResponse
from tastypie.authorization import Authorization

from tasks.models import Task, SubTask


def get_seconds_difference(now, current_date):
    return (now - current_date).total_seconds() > 0


class SubTaskResource(ModelResource):
    class Meta:
        queryset = SubTask.objects.all().order_by("sub_due_date")
        resource_name = 'sub_tasks'
        fields = ['sub_title', 'sub_description', 'sub_due_date', 'sub_state']
        filtering = {
            'sub_title': ALL,
        }


class TaskResource(ModelResource):
    sub_tasks_many = fields.ManyToManyField(SubTaskResource, 'sub_task_many', full=True, null=True, blank=True)

    class Meta:
        queryset = Task.objects.all().order_by("due_date")
        resource_name = 'tasks'
        fields = ['sub_tasks_many', 'title', 'description', 'due_date', 'state']
        filtering = {
            'title': ALL,
        }


class DueDateTodayResource(ModelResource):
    sub_tasks_many = fields.ManyToManyField(SubTaskResource, 'sub_task_many', full=True, null=True, blank=True)

    class Meta:
        today = date.today()
        queryset = Task.objects.all().filter(due_date__year=today.year,
                                             due_date__month=today.month,
                                             due_date__day=today.day).order_by("due_date")
        resource_name = 'due_date_today'
        fields = ['title', 'description', 'due_date', 'state', 'sub_tasks_many']
        filtering = {
            'title': ALL,
        }


class DueDateThisWeekResource(ModelResource):
    sub_tasks_many = fields.ManyToManyField(SubTaskResource, 'sub_task_many', full=True, null=True, blank=True)

    class Meta:
        today = date.today().strftime("%Y/%m/%d")
        dt = datetime.strptime(today, '%Y/%m/%d')
        start = dt - timedelta(days=dt.weekday())
        end = start + timedelta(days=6)
        queryset = Task.objects.all().filter(due_date__range=(start, end))

        resource_name = 'due_date_this_week'
        fields = ['title', 'description', 'due_date', 'state', 'sub_tasks_many']
        filtering = {
            'title': ALL,
        }


class DueDateNextWeekResource(ModelResource):
    sub_tasks_many = fields.ManyToManyField(SubTaskResource, 'sub_task_many', full=True, null=True, blank=True)

    class Meta:
        today = date.today().strftime("%Y/%m/%d")
        dt = datetime.strptime(today, '%Y/%m/%d')
        start = dt - timedelta(days=dt.weekday()) + timedelta(days=7)
        end = start + timedelta(days=6)

        queryset = Task.objects.all().filter(due_date__range=(start, end)).order_by("due_date")
        resource_name = 'due_date_next_week'
        fields = ['title', 'description', 'due_date', 'state', 'sub_tasks_many']
        filtering = {
            'title': ALL,
        }


class DueDateOverdueResource(ModelResource):
    sub_tasks_many = fields.ManyToManyField(SubTaskResource, 'sub_task_many', full=True, null=True, blank=True)

    # tasks = Task.objects.all()
    # for task in tasks:
    #     d2 = datetime(task.due_date.year, task.due_date.month, task.due_date.day, task.due_date.hour,
    #                   task.due_date.minute, task.due_date.second)
    #     overdue_task = get_seconds_difference(datetime.now(), d2)
    #     if overdue_task:
    #         OverDueTask = Task(overdue_task)
    #         OverDueTask.save()

    class Meta:
        today = date.today().strftime("%Y-%m-%d")
        queryset = Task.objects.all().filter(due_date__lte=today).order_by("due_date")
        resource_name = 'due_date_overdue'
        fields = ['title', 'description', 'due_date', 'state', 'sub_tasks_many']
        filtering = {
            'title': ALL,
        }
