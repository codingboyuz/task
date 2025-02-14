from  django.urls import path

from subtask.views import *


app_name = "SubTask"
urlpatterns =[

    path('subtask/create/',SubTaskCreateApiView.as_view(),name='subtask-create'),
    path('subtask/list/',SubTaskListApiView.as_view(),name='subtask-list'),
    path('subtask/priority/',SubTaskPriorityFilterApiView.as_view(),name='priority'),
    path('subtask/status/',SubTaskStatusFilterApiView.as_view(),name='sub_status'),

    path('subtask/update/<uuid:id>/', SubTaskUpdateAPIView.as_view(), name='subtask-update'),
    path('subtask/delete/<uuid:id>/',SubTaskDeleteAPIView.as_view(),name='sub_update'),
]