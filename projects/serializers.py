from rest_framework import serializers
from .models import Project
from clients.models import Client
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.client_name')
    users = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'client_name', 'users', 'created_at', 'created_by']

    def get_users(self, obj):
        return [user.username for user in obj.users.all()]
