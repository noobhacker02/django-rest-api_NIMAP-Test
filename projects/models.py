from django.db import models
from django.db import models
from django.contrib.auth.models import User
from clients.models import Client

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')

    def __str__(self):
        return self.project_name

# Create your models here.
