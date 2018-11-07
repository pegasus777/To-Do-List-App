from django.conf.urls import url
from . import views


app_name = 'tasks'


urlpatterns = [
    #/update/api/v1/tasks/21/
    url(r'^api/v1/tasks/(?P<tasks_id>\d+)/$', views.update, name='update'),

    url(r'^api/v1/sub_tasks/(?P<tasks_id>\d+)/$', views.sub_task_update, name='sub_task_update'),

    url(r'^api2/due_date_today/(?P<tasks_id>\d+)/$', views.update, name='update'),

    url(r'^api2/due_date_this_week/(?P<tasks_id>\d+)/$', views.update, name='update'),

    url(r'^api2/due_date_next_week/(?P<tasks_id>\d+)/$', views.update, name='update'),

    url(r'^api2/due_date_overdue/(?P<tasks_id>\d+)/$', views.update, name='update'),

]