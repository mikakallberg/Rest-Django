""" Contacts """
from django.db import models
from django.contrib.auth.models import User


class Contacts(models.Model):
    """ Model for list of active chats """
    owner = models.ForeignKey(
        User,
        related_name='contacts_owner',
        on_delete=models.CASCADE)
    contact = models.ForeignKey(
        User,
        related_name='contacts_contact',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)

    class Meta:
        """ Order of view and order for unique chat """
        ordering = ['updated_at']
        unique_together = ['owner', 'contact']

    def __str__(self):
        return f'{self.owner} {self.contact}'
