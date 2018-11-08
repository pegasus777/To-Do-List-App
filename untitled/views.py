from django.http import HttpResponse
from django.contrib import messages

# importing loading from django template
from django.template import loader
from django.shortcuts import render
from tasks.models import Task, SubTask
from datetime import datetime, date, timedelta
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


# our view which is a function named index
def index(request):
    utc = pytz.UTC
    # using utc because it can be used globally
    tasks = Task.objects.all()

    task_alert = []
    for task in tasks:
        time_between_insertion = datetime.now().replace(tzinfo=utc) - timedelta(days=30)
        if task.due_date.replace(tzinfo=utc) < time_between_insertion:
            # print ("The insertion date is older than 30 days")
            # print(task.title)
            task.delete()
            continue
        # else:
        #   print ("The insertion date is not older than 30 days")

        alert = get_hours_difference(task.due_date)
        if alert:
            print(task.title)
            print (task.due_date)
            if not task.state:
                task_alert.append(task)

    return render(request, 'index.html', {'all_tasks': task_alert})

    # getting our template
    # template = loader.get_template('index.html')
    #
    # # rendering the template in HttpResponse
    # return HttpResponse(template.render())




