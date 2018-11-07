"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.a,s_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from untitled import views
from tasks import apps
from tasks.api import TaskResource, DueDateTodayResource, SubTaskResource, DueDateThisWeekResource, \
    DueDateNextWeekResource, DueDateOverdueResource
from tastypie.api import Api

task_resource = TaskResource()
due_date_resource = DueDateTodayResource()
due_date_this_week_resource = DueDateThisWeekResource()
due_date_next_week_resource = DueDateNextWeekResource()
due_date_overdue_resource = DueDateOverdueResource()

app_name = 'home'

v1_api = Api(api_name='v1')
v1_api.register(TaskResource())
v1_api.register(SubTaskResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^update/', include('tasks.urls')),
    url(r'^$', views.index),
    url(r'^api/', include(v1_api.urls)),
    url(r'^api2/', include(due_date_resource.urls)),
    url(r'^api2/', include(due_date_this_week_resource.urls)),
    url(r'^api2/', include(due_date_next_week_resource.urls)),
    url(r'^api2/', include(due_date_overdue_resource.urls)),


]
