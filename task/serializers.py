from .models import TaskModel
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'


    def validate_title(self, value):
        if not value.strip():  # Check if the title is empty or just spaces
            raise serializers.ValidationError("Please Enter some title  value.")
        return value