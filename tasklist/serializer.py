from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from tasklist.models import SubTask, Task


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
        print("Validated Data:", validated_data)

        # Task ID tekshirish
        task_id = validated_data.pop('task', None)
        print("###########################################task_id#################################################")
        print(task_id)
        print("############################################################################################")
        if not task_id:
            raise serializers.ValidationError({"task": "Task ID is required."})

        try:
            print(
                "###########################################task_id2#################################################")
            print(task_id)
            print("############################################################################################")
            # Task obyektini bazadan olish
            task = Task.objects.get(id=task_id)
            print("############################################################################################")
            print(task)
            print("############################################################################################")
        except Task.DoesNotExist:
            raise serializers.ValidationError({"task": "Task not found."})

        # Task obyektini validated_data ichiga qo‘shish
        validated_data['task'] = task

        # SubTask yaratish
        sub_task = SubTask.objects.create(**validated_data)
        return sub_task


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
