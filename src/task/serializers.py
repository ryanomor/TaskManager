from rest_framework import serializers
from task.models import TaskItem

class TaskItemSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.ReadOnlyField()
    class Meta:
        model = TaskItem
        fields = ('title', 'completed', 'description', 'url', 'order', 'due_date')
