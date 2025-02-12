from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from tasklist.models import Task, SubTask
from django.core.cache import cache

from tasklist.serializer import TaskSerializer, SubTaskSerializer, SubTaskCreateSerializer


class TaskListApiView(APIView):
    def get(self, request):
        try:
            task = Task.objects.all().order_by("-created_time")
            serializer = TaskSerializer(task, many=True)

            if serializer.data:
                data = {
                    'success': True,
                    'data': serializer.data,
                    'message': 'Task list successfully get'
                }
                return Response(data=data, status=status.HTTP_200_OK)
            data = {
                'success': False,
                'data': serializer.error_messages,
                'message': 'Task list error get'
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            data = {
                'success': False,
                'message': f'Exception {str(e)}'
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

class TaskCreateApiView(APIView):
    @swagger_auto_schema(request_body=TaskSerializer)
    def post(self, request):
        try:
            serializer = TaskSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                data = {"success": True, "message": "Successfuly created task"}
                return Response(data=data, status=status.HTTP_201_CREATED)
            data = {"success": False, "message": "Error created task"}

            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            data = {"success": False, "message": f"Error  {str(e)}"}

            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

class SubTaskCreateApiView(APIView):
    @swagger_auto_schema(request_body=SubTaskCreateSerializer)
    def post(self, request):

        try:
            serializer = SubTaskCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                data = {
                    'success': True,
                    'message': "SubTask successfully created"
                }
                return Response(data=data, status=status.HTTP_201_CREATED)
        except Exception as e:

            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)



class SubTaskListApiView(APIView):
    def get(self, request):
        try:
            task = SubTask.objects.all().order_by("-created_time")
            serializer = SubTaskSerializer(task, many=True)

            if serializer.data:
                data = {
                    'success': True,
                    'data': serializer.data,
                    'message': 'SubTask list successfully get'
                }
                return Response(data=data, status=status.HTTP_200_OK)
            data = {
                'success': False,
                'data': serializer.error_messages,
                'message': 'SubTask list error get'
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            data = {
                'success': False,
                'message': f'Exception {str(e)}'
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)