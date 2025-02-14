from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tasklist.models import Task
from tasklist.serializer import TaskSerializer, TaskUpdateSerializer


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
    # @swagger_auto_schema(request_body=TaskSerializer)
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

class TaskPriorityFilterApiView(APIView):
    # @swagger_auto_schema(manual_parameters=[
    #     openapi.Parameter(
    #         'priority',
    #         openapi.IN_QUERY,
    #         description="Bu api yo'lining maqsadi tasklarni bajariladigan ->(low, medium, high)larni  filterlanib beradi",
    #         type=openapi.TYPE_STRING,
    #         required=True
    #     )
    # ])
    def get(self, request):
        try:
            # Priority parametresini olish

            priority = request.query_params.get('priority')
            if not priority:
                return Response({"error": "Priority is required"}, status=status.HTTP_400_BAD_REQUEST)

            tasks = Task.objects.filter(priority=priority)
            serializer = TaskSerializer(tasks, many=True)

            # Javobni shakllantirish
            data = {
                'success': True,
                'data': serializer.data,
                'message': f'Tasks filtered by priority: {priority}'
            }
            return Response(data=data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TaskStatusFilterApiView(APIView):
    # @swagger_auto_schema(manual_parameters=[
    #     openapi.Parameter(
    #         'status',
    #         openapi.IN_QUERY,
    #         description="Bu api yo'lining maqsadi tasklarni bajariladigan ->(low, medium, high)larni  filterlanib beradi",
    #         type=openapi.TYPE_STRING,
    #         required=True
    #     )
    # ])
    def get(self, request):
        try:
            # Priority parametresini olish

            task_status = request.query_params.get('status')
            if not task_status:
                return Response({"error": "Status is required"}, status=status.HTTP_400_BAD_REQUEST)

            tasks = Task.objects.filter(status=task_status)
            serializer = TaskSerializer(tasks, many=True)

            # Javobni shakllantirish
            data = {
                'success': True,
                'data': serializer.data,
                'message': f'Tasks filtered by status: {task_status}'
            }
            return Response(data=data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TaskUpdateAPIView(APIView):

    def put(self, request, id):
        try:
            subtask = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskUpdateSerializer(subtask, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Task updated successfully', 'data': serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDeleteAPIView(APIView):
    def delete(self, request, id):
        try:
            sub_task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        sub_task.delete()
        return Response({"message": "Task deleted successfully."}, status=status.HTTP_204_NO_CONTENT)