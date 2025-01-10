from django_filters import rest_framework as filters
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import TaskModel as Task, CustomUser as User
from .serializers import TaskSerializer, UserSerializer
from datetime import datetime

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class TaskFilter(filters.FilterSet):
    status = filters.ChoiceFilter(choices=Task.STATUS_CHOICES, label="Status")
    priority = filters.ChoiceFilter(choices=Task.PRIORITY_CHOICES, label="Priority")
    due_date = filters.DateFilter(field_name='due_date', lookup_expr='gte', label='Due Date (gte)')

    class Meta:
        model = Task
        fields = ['status', 'priority', 'due_date']

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = TaskFilter
    ordering_fields = ['due_date', 'priority'] 
    ordering = ['due_date']

    def get_queryset(self):
        # filter tasks by the current user
        return Task.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        # save tasks with the owner field set to the current user
        serializer.save(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.status == 'Completed':
            return Response(
                {'error': 'Cannot edit a completed task'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        # Default update behavior
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        task = self.get_object()
        status_data = request.data.get('status')
        if task.status == 'Completed' and status_data == 'Pending':
            #clear completed_at field if the task status is marked as pending
            task.completed_at = None
            task.save()
        elif status_data == 'Completed':
            task.completed_at = datetime.now()
            task.save()
        # Default partial_update behavior
        return super().partial_update(request, *args, **kwargs)

