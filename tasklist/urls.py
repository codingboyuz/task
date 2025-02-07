

from django.urls import path

from tasklist.views import DepartamentCreateApiView, DepartamentListApiView, DepartamentByIdApiView, \
    DepartamentDeleteApiView, DepartmentTaskDetailApiView, TaskListApiView, TaskByIdApiView, TaskCreateApiView, \
    TaskDeleteApiView, DepartmentLookupView

urlpatterns = [
    path('department/login', DepartmentLookupView.as_view(), name='login'),
    path('department/create', DepartamentCreateApiView.as_view(), name='create'),
    path('department/list', DepartamentListApiView.as_view(), name='list'),
    path('department/<int:pk>/', DepartamentByIdApiView.as_view(), name='department-detail'),
    path('department/<int:pk>/task/', DepartmentTaskDetailApiView.as_view(), name='department-task-detail'),
    path('department/<int:pk>/delete/', DepartamentDeleteApiView.as_view(), name='department-delete'),

    path('task/create', TaskCreateApiView.as_view(), name='create'),
    path('task/list', TaskListApiView.as_view(), name='list'),
    path('task/<int:pk>/', TaskByIdApiView.as_view(), name='task-detail'),
    path('task/<int:pk>/delete/', TaskDeleteApiView.as_view(), name='task-delete'),
]
