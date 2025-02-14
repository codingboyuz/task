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

class TaskUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=300)
    description = serializers.CharField()
    status = serializers.CharField(max_length=20)
    priority = serializers.CharField(max_length=20)
    due_date = serializers.DateTimeField()
    updated_time = serializers.DateTimeField(read_only=True)

    def update(self, instance, validated_data):
        # Task ni alohida qayta ishlash
        task_uuid = validated_data.get('task')
        if task_uuid:
            try:
                task_instance = Task.objects.get(id=task_uuid)
                instance.task = task_instance
            except Task.DoesNotExist:
                raise serializers.ValidationError({'task': 'Task with this ID does not exist'})

        # Qolgan maydonlarni yangilash
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.due_date = validated_data.get('due_date', instance.due_date)

        instance.save()
        return instance