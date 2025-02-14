from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from subtask.models import SubTask
from drf_yasg import openapi
from subtask.serializer import SubTaskSerializer, SubTaskCreateSerializer, SubTaskUpdateSerializer


class SubTaskCreateApiView(APIView):
    # @swagger_auto_schema(request_body=SubTaskCreateSerializer)
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
            subtasks = SubTask.objects.all().order_by("-created_time")  # `created_time` maydonini tekshirib chiqing
            serializer = SubTaskSerializer(subtasks, many=True)

            # Agar serializerda ma'lumot bo'lsa
            if serializer.data:
                data = {
                    'success': True,
                    'data': serializer.data,
                    'message': 'SubTask list successfully retrieved'
                }
                return Response(data=data, status=status.HTTP_200_OK)

            # Agar ma'lumot bo'lmasa, xato qaytarish
            data = {
                'success': False,
                'data': "No data found",
                'message': 'No SubTasks available'
            }
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Har qanday xatolikni qaytarish
            data = {
                'success': False,
                'message': f'Error occurred: {str(e)}'
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class SubTaskPriorityFilterApiView(APIView):
    # @swagger_auto_schema(manual_parameters=[
    #     openapi.Parameter(
    #         'priority',
    #         openapi.IN_QUERY,
    #         description="Bu api yo'lining maqsadi subtasklarni bajariladigan ->(low, medium, high)larni  filterlanib beradi",
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
    # @swagger_auto_schema(manual_parameters=[
    #     openapi.Parameter(
    #         'status',
    #         openapi.IN_QUERY,
    #         description="Bu api yo'lining maqsadi subtasklarni bajariladigan ->(low, medium, high)larni  filterlanib beradi",
    #         type=openapi.TYPE_STRING,
    #         required=True
    #     )
    # ])
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


class SubTaskUpdateAPIView(APIView):
    # @swagger_auto_schema(request_body=SubTaskUpdateSerializer)
    def put(self, request, id):
        try:
            subtask = SubTask.objects.get(id=id)
        except SubTask.DoesNotExist:
            return Response({'error': 'SubTask not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubTaskUpdateSerializer(subtask, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'SubTask updated successfully', 'data': serializer.data},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubTaskDeleteAPIView(APIView):
    def delete(self, request, id):
        try:
            sub_task = SubTask.objects.get(id=id)
        except SubTask.DoesNotExist:
            return Response({"error": "SubTask not found."}, status=status.HTTP_404_NOT_FOUND)

        sub_task.delete()
        return Response({"message": "SubTask deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
