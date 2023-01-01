
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TodoSerializer
from .models import Todo

class TodoViewSet(viewsets.ModelViewSet):

    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer
