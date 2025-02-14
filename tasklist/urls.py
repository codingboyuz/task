from  django.urls import path

from tasklist.views import *


app_name = "Task"
urlpatterns =[
    path('task/create/',TaskCreateApiView.as_view(),name='create'),
    path('task/list/',TaskListApiView.as_view(),name='list'),
    path('task/priority/',TaskPriorityFilterApiView.as_view(),name='priority'),
    path('task/status/',TaskStatusFilterApiView.as_view(),name='task_status'),
    path('task/update/<uuid:id>/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('task/delete/<uuid:id>/', TaskDeleteAPIView.as_view(), name='task_delete'),
]