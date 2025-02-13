from  django.urls import path

from subtask.views import *


app_name = "SubTask"
urlpatterns =[

    path('create/',SubTaskCreateApiView.as_view(),name='subtask-create'),
    path('list/',SubTaskListApiView.as_view(),name='subtask-list'),
    path('priority/',SubTaskPriorityFilterApiView.as_view(),name='priority'),
    path('status/',SubTaskStatusFilterApiView.as_view(),name='sub_status'),

    path('subtasks/', SubTaskUpdateAPIView.as_view(), name='subtask-update'),
    path('delete/<uuid:pk>/',SubTaskDeleteAPIView.as_view(),name='sub_update'),
]