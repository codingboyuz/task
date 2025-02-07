from rest_framework import serializers
from .models import Department, Task



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'department', 'title','task_setter', 'description', 'due_date', 'created_at',]

        extra_kwargs = {
            'created_at': {'read_only': True},
        }


class DepartmentSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Department
        fields = ['id', 'name','tasks']

        extra_kwargs = {
            'tasks': {'read_only': True},
        }


class DepartmentTaskSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Department
        fields = ['id','tasks']



class DepartmentLookupSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate_name(self, value):
        try:
            department = Department.objects.get(name=value)
            return {"id": department.id, "name": department.name}
        except Department.DoesNotExist:
            raise serializers.ValidationError("Bunday department mavjud emas")


