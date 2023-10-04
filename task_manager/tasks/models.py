from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    completion_status = models.BooleanField(default=False)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_update_datetime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional profile fields (e.g., profile picture, bio, etc.)

    def __str__(self):
        return self.user.username
    
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for {self.task.title}"
