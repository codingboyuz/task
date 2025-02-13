from  django.urls import path
from rest_framework.urls import app_name

from tasklist.views import *


app_name = "Task"
urlpatterns =[
    path('create/',TaskCreateApiView.as_view(),name='create'),
    path('list/',TaskListApiView.as_view(),name='list'),
    path('priority/',TaskPriorityFilterApiView.as_view(),name='priority'),
    path('status/',TaskStatusFilterApiView.as_view(),name='task_status'),
]