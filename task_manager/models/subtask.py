from django.db import models
from .task import Task

class SubTask(models.Model):
    STATUS_CHOICES = Task.STATUS_CHOICES

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_subtask'
        verbose_name = 'SubTask'
        ordering = ['-created_at']
