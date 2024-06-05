import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycalendar.settings')
django.setup()

from django.test import TestCase
from django.core.management import call_command
from django.utils import timezone
from unittest.mock import patch
from .models import Event
from django.contrib.auth.models import User

# Unit Tests for Reminder Notifications
class ReminderNotificationTests(TestCase):
    def test_handle_sends_reminder_for_upcoming_event(self):
        user = User.objects.create(username='test_user', email='test@example.com')

        today = timezone.now()
        event_date = today.date()
        event_time = today.time()

        creator = User.objects.create(username='creator_user', email='creator@example.com')

        event = Event.objects.create(
            title='Test Event',
            date=event_date,
            start_time=event_time,
            end_time=event_time,
            creator=creator
        )
        event.invited_users.add(user)

        with patch('main.models.Event.objects.filter') as mock_filter:
            mock_filter.return_value = [event]

            with patch('django.core.mail.send_mail') as mock_send_mail:
                call_command('create_reminders')

                mock_send_mail(
                    'Upcoming Event Reminder',
                    f'Don\'t forget! You have an event "{event.title}" scheduled for {event.date} at {event.start_time}.',
                    'husakmaria74@email.com',
                    [creator.email],
                    fail_silently=False,
                )