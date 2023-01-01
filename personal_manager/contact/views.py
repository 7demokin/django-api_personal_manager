
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ContactSerializer
from .models import Contact

class ContactViewSet(viewsets.ModelViewSet):

    queryset = Contact.objects.all().order_by('-id')
    serializer_class = ContactSerializer
