from  django.urls import path
from rest_framework.urls import app_name

from tasklist.views import *


app_name = "Task"
urlpatterns =[
    path('task/create/',TaskCreateApiView.as_view(),name='create'),
    path('task/list/',TaskListApiView.as_view(),name='list'),
    path('task/priority/',TaskPriorityFilterApiView.as_view(),name='priority'),
    path('task/status/',TaskStatusFilterApiView.as_view(),name='task_status'),
]