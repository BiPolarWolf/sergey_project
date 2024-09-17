from django.shortcuts import render
from . import models,serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TaskListCreateView(ListCreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if isinstance(self.request.user, User):
            return super().get_queryset().filter(owner=self.request.user)
        return super().get_queryset()
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return serializers.TaskCreateSerializer
        return serializers.TaskSerializer
    


class TaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskCreateSerializer
    permission_classes = [IsOwner]

    
