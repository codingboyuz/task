from  django.urls import path
from rest_framework.urls import app_name

from tasklist.views import *


app_name = "Task"
urlpatterns =[
    path('task/create/',TaskCreateApiView.as_view(),name='create'),
    path('task/list/',TaskListApiView.as_view(),name='list'),


    path('subtask/create/',SubTaskCreateApiView.as_view(),name='subtask-create'),
    path('subtask/list/',SubTaskListApiView.as_view(),name='subtask-list'),
]