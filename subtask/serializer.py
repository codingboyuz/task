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
                  'updated_time',]

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