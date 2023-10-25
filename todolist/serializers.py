from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    created = serializers.DateField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Task
        fields = "__all__"
