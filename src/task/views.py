from task.models import TaskItem
from task.serializers import TaskItemSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework.decorators import list_route
from rest_framework.response import Response

# Create your views here.
class TaskItemViewSet(viewsets.ModelViewSet):
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer

    def perform_create(self, serializer):
        # Save instance to get primary key and then update URL
        instance = serializer.save()
        instance.url = reverse('taskitem-detail', args=[instance.pk], request=self.request)
        instance.save()

    # Deletes all task items
    def delete(self, request):
        TaskItem.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
