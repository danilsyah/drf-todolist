from dataclasses import fields
from rest_framework import serializers
from apps.todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()
    
    class Meta:
        model = Todo
        fields = ['id','title','memo','created','completed']
        

class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['title','memo','created','completed']