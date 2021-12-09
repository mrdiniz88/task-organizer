from django.db import models
from User.models import User

class Projects(models.Model):
    name = models.CharField(max_length = 100)
    # description = models.TextField()
    finish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

class Tasks(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    finish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='projects')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'