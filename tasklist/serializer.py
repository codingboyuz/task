from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from subtask.serializer import SubTaskSerializer
from tasklist.models import  Task




class TaskSerializer(serializers.ModelSerializer):
    sub_tasks = SubTaskSerializer(many=True, read_only=True)  # Task ichida sub_task larni chiqarish
    created_time = serializers.DateTimeField(read_only=True)
    updated_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title',
                  'description',
                  'status',
                  'priority',
                  'due_date',
                  'sub_tasks',
                  'created_time',
                  'updated_time',
                  ]  # Barcha maydonlar + sub_task lar

        extra_kwargs = {
            "sub_tasks": {"read_only": True},
            "updated_time": {"read_only": True},
            "created_time": {"read_only": True},
        }

