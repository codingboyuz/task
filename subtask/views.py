from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from subtask.models import  SubTask
from drf_yasg import openapi
from subtask.serializer import  SubTaskSerializer, SubTaskCreateSerializer


class SubTaskCreateApiView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["task"],
            properties={
                "task": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Taskga biriktirish uchun Task ID sini kiriting"
                ),
                "title": openapi.Schema(type=openapi.TYPE_STRING, description="SubTask sarlavhasi"),
                "description": openapi.Schema(type=openapi.TYPE_STRING, description="SubTask tavsifi"),
                "status": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    enum=["pending", "in_progress", "completed"],
                    description="SubTask holati"
                ),
                "priority": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    enum=["low", "medium", "high"],
                    description="SubTask ustuvorligi"
                ),
                "due_date": openapi.Schema(type=openapi.TYPE_STRING, format="date-time",
                                           description="SubTask uchun belgilangan sana va vaqt")
            }
        ),
        operation_description="SubTask yaratish va Taskga bog‘lash uchun POST so‘rovi"
    )
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

class SubTaskPriorityFilterApiView(APIView):
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            'priority',
            openapi.IN_QUERY,
            description="Bu api yo'lining maqsadi subtasklarni bajariladigan ->(low, medium, high)larni  filterlanib beradi",
            type=openapi.TYPE_STRING,
            required=True
        )
    ])
    def get(self, request):
        try:
            # Priority parametresini olish

            priority = request.query_params.get('priority')
            if not priority:
                return Response({"error": "Priority is required"}, status=status.HTTP_400_BAD_REQUEST)

            tasks = SubTask.objects.filter(priority=priority)
            serializer = SubTaskSerializer(tasks, many=True)

            # Javobni shakllantirish
            data = {
                'success': True,
                'data': serializer.data,
                'message': f'Tasks filtered by priority: {priority}'
            }
            return Response(data=data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SubTaskStatusFilterApiView(APIView):
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            'status',
            openapi.IN_QUERY,
            description="Bu api yo'lining maqsadi subtasklarni bajariladigan ->(low, medium, high)larni  filterlanib beradi",
            type=openapi.TYPE_STRING,
            required=True
        )
    ])
    def get(self, request):
        try:
            # Priority parametresini olish

            sub_status = request.query_params.get('status')
            if not sub_status:
                return Response({"error": "Priority is required"}, status=status.HTTP_400_BAD_REQUEST)

            tasks = SubTask.objects.filter(status=sub_status)
            serializer = SubTaskSerializer(tasks, many=True)

            # Javobni shakllantirish
            data = {
                'success': True,
                'data': serializer.data,
                'message': f'Tasks filtered by priority: {sub_status}'
            }
            return Response(data=data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)