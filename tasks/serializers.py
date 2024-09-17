from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),required=False)
    
    class Meta:
        model = models.Task
        fields = '__all__'


class TaskCreateSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='tasks-detail',lookup_field='pk',read_only=True)
    class Meta:
        model = models.Task
        fields = ['url','title','description','date','status']
    