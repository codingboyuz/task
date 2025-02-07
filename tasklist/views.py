from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from tasklist.serializer import DepartmentSerializer, TaskSerializer,DepartmentLookupSerializer

from rest_framework import status
from tasklist.models import Department, Task

class DepartmentLookupView(APIView):
    @swagger_auto_schema(request_body=DepartmentLookupSerializer)
    def post(self, request):
        serializer = DepartmentLookupSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartamentCreateApiView(APIView):
    @swagger_auto_schema(request_body=DepartmentSerializer)
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'success': True,
                    'data': serializer.data,
                    'message': "Success"}
            return Response(data=data, status=status.HTTP_200_OK)
        data = {'success': False,
                'data': serializer.errors,
                'message': "Error"}
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)


class DepartamentListApiView(APIView):
    def get(self, request):
        try:
            dep = Department.objects.all()
            if not dep:  # Agar bo'sh bo'lsa
                return Response(
                    {"success": False, "message": "Department null."},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = DepartmentSerializer(dep, many=True)
            if serializer.data:
                data = {'success': True, 'data': serializer.data, 'message': "Success data"}
                return Response(data=data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"success": False,
                             "error": str(e), }, status=status.HTTP_400_BAD_REQUEST)


class DepartamentByIdApiView(APIView):
    def get(self, request, pk):  # pk (primary key) parametrini olish
        try:
            dep = Department.objects.get(id=pk)  # id bo'yicha izlash
            serializer = DepartmentSerializer(dep)
            data = {'success': True, 'data': serializer.data, 'message': "Success data"}
            return Response(data=data, status=status.HTTP_200_OK)
        except Department.DoesNotExist:
            return Response({"success": False, "message": "Department not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DepartamentDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            # Departamentni pk orqali olish
            department = Department.objects.get(pk=pk)
            department.delete()  # O'chirish
            return Response(
                {"success": True, "message": "Department deleted successfully."},
                status=status.HTTP_200_OK
            )
        except Department.DoesNotExist:
            return Response(
                {"success": False, "message": "Department not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )



class DepartmentTaskDetailApiView(APIView):
    def get(self, request, pk):
        try:
            department = Department.objects.get(id=pk)  # Departmentni id orqali olish
            serializer = DepartmentSerializer(department)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Department.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Department not found.'
            }, status=status.HTTP_404_NOT_FOUND)



class TaskCreateApiView(APIView):
    @swagger_auto_schema(request_body=TaskSerializer)
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {'success': True,
                    'data': serializer.data,
                    'message': "Success"}
            return Response(data=data, status=status.HTTP_200_OK)
        data = {'success': False,
                'data': serializer.errors,
                'message': "Error"}
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)


class TaskListApiView(APIView):
    def get(self, request):
        try:
            dep = Task.objects.all()
            if not dep:  # Agar bo'sh bo'lsa
                return Response(
                    {"success": False, "message": "Department null."},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = TaskSerializer(dep, many=True)
            if serializer.data:
                data = {'success': True, 'data': serializer.data, 'message': "Success data"}
                return Response(data=data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"success": False,
                             "error": str(e), }, status=status.HTTP_400_BAD_REQUEST)


class TaskByIdApiView(APIView):
    def get(self, request, pk):  # pk (primary key) parametrini olish
        try:
            task = Task.objects.get(id=pk)  # id bo'yicha izlash
            if not task:
                return Response(
                    {"success": False, "message": "Department null."},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = TaskSerializer(task)
            data = {'success': True, 'data': serializer.data, 'message': "Success data"}
            return Response(data=data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"success": False, "message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"success": False, "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class TaskDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            # Departamentni pk orqali olish
            department = Task.objects.get(pk=pk)
            department.delete()  # O'chirish
            return Response(
                {"success": True, "message": "Department deleted successfully."},
                status=status.HTTP_200_OK
            )
        except Task.DoesNotExist:
            return Response(
                {"success": False, "message": "Department not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"success": False, "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
