from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    RECURRENCE_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]
    recurrence = models.CharField(max_length=10, choices=RECURRENCE_CHOICES, blank=True, null=True)

    EVENT_TYPE_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]
    event_type = models.CharField(max_length=10, choices=EVENT_TYPE_CHOICES, default='offline')

    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('social', 'Social'),
        ('holiday', 'Holiday'),
        ('education', 'Education'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    invited_users = models.ManyToManyField(User, related_name='invited_events')
    attendees = models.ManyToManyField(User, related_name='attended_events')

    def __str__(self):
        return self.title


