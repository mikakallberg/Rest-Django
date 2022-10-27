""" Messages view """
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Message
from .serializers import MessageSerializer, MessageDetailSerializer


@method_decorator(login_required, name='dispatch')
class MessageList(generics.ListCreateAPIView):
    """ List all messages and create messages"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@method_decorator(login_required, name='dispatch')
class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    The detail view of a authenticated user that
    is following another user
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Message.objects.all()
    serializer_class = MessageDetailSerializer
