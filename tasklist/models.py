from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    department = models.ForeignKey(Department, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    task_setter =models.CharField(max_length=300)
    description = models.TextField()
    due_date = models.CharField(max_length=100)  # Bu qiymatni foydalanuvchi yoki tizim tomonidan qo'yish mumkin
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
