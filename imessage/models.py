""" Messages """
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """ Model for chat messages """
    owner = models.ForeignKey(
        User,
        related_name='message_owner',
        on_delete=models.CASCADE)
    contact = models.ForeignKey(
        User,
        related_name='message_contact',
        on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(
        upload_to='images/', default=None, blank=True
    )
    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]
    image_filter = models.CharField(
        max_length=12, choices=image_filter_choices, default='normal'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Ordering messages """
        ordering = ['-created_at']

    def __str__(self):
        """ Returning content """
        return f'{self.owner} {self.contact} {self.content}'
