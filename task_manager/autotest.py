import os
import django
from datetime import timedelta
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from task_manager.models.task import Task
from task_manager.models.subtask import SubTask

#============================CREATE=============================================================
# Create task
task = Task.objects.create(
    title="Prepare presentation",
    description="Prepare materials and slides for the presentation",
    status="New",
    deadline=timezone.now() + timedelta(days=3)
)
print(f"Created task: {task.title}")

# Create subtask
subtask = SubTask.objects.create(
    title="Gather information",
    description="Find necessary information for the presentation",
    status="New",
    deadline=timezone.now() + timedelta(days=2),
    task=task
)
print(f"Created subtask: {subtask.title} of task: {task.title}")

SubTask.objects.create(
    title="Create slides",
    description="Create presentation slides",
    status="New",
    deadline=timezone.now() + timedelta(days=1),
    task=task
)
print(f"Created subtask: {subtask.title} of task: {task.title}")

#============================READ=============================================================
# Read tasks
tasks = Task.objects.filter(status="New")
for task in tasks:
    print(f"Read task: {task.title}")

# Read subtasks
subtasks = SubTask.objects.filter(status="Done", deadline__lt=timezone.now())
for subtask in subtasks:
    print(f"Read subtask: {subtask.title} of task: {subtask.title}")

#============================UPDATE=============================================================

# Update status
task = Task.objects.get(title="Prepare presentation")
task.status = "In progress"
task.save()
print(f"Update task status: {task.title} new status: {task.status}")

# Update deadline
subtask1 = SubTask.objects.get(title="Gather information")
subtask1.deadline = timezone.now() - timedelta(days=2)
subtask1.save()
print(f"Update subtask deadline: {subtask1.title} new deadline: {subtask1.deadline}")

# Update description
subtask2 = SubTask.objects.get(title="Create slides")
subtask2.description = "Create and format presentation slides"
subtask2.save()
print(f"Update subtask description: {subtask2.title} new description: {subtask2.description}")


#============================DELETE=============================================================
task = Task.objects.get(title="Prepare presentation")
task.delete()
deleted_task = Task.objects.filter(title="Prepare presentation").first()
if not deleted_task:
    print("No task by title Prepare presentation")
