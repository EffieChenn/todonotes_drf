from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer


# Create your views here.
class TaskListView(ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
