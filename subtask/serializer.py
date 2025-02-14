import uuid

from rest_framework import serializers

from subtask.models import SubTask
from tasklist.models import Task


class SubTaskSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(read_only=True)
    updated_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = SubTask
        fields = ['id',
                  'task',
                  'title',
                  'description',
                  'status',
                  'priority',
                  'due_date',
                  'created_time',
                  'updated_time', ]

        extra_kwargs = {
            "updated_time": {"read_only": True},
            "created_time": {"read_only": True},
        }


class SubTaskCreateSerializer(serializers.ModelSerializer):
    task = serializers.UUIDField()
    created_time = serializers.DateTimeField(read_only=True)
    updated_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = SubTask
        fields = '__all__'

        extra_kwargs = {
            "updated_time": {"read_only": True},
            "created_time": {"read_only": True},
        }

    def create(self, validated_data):
        # Task ID tekshirish
        task_id = validated_data.pop('task', None)
        if not task_id:
            raise serializers.ValidationError({"task": "Task ID is required."})

        try:
            # Task obyektini bazadan olish
            task = Task.objects.get(id=task_id)

        except Task.DoesNotExist:
            raise serializers.ValidationError({"task": "Task not found."})

        # Task obyektini validated_data ichiga qo‘shish
        validated_data['task'] = task

        # SubTask yaratish
        sub_task = SubTask.objects.create(**validated_data)
        return sub_task


class SubTaskUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=300)
    description = serializers.CharField()
    task = serializers.UUIDField()
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

