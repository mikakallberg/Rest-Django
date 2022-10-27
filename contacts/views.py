""" Contacts view """
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from contacts.models import Contacts
from .serializers import ContactsSerializer, ContactsDetailSerializer


@method_decorator(login_required, name='dispatch')
class ContactList(generics.ListCreateAPIView):
    """
    List all contacts
    contacts = authenticated users in active chats with User
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@method_decorator(login_required, name='dispatch')
class ContactDetailList(generics.RetrieveUpdateDestroyAPIView):
    """
    List all contacts
    contacts = authenticated users in active chats with User
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Contacts.objects.all()
    serializer_class = ContactsDetailSerializer
