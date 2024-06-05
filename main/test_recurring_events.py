import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycalendar.settings')
django.setup()

from django.test import TestCase
from .models import Event, User
from django.urls import reverse
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User



# Unit Tests for Recurring Events
class EventTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', password='testpassword')
        self.event_data = {
            'title': 'Test Event',
            'date': '2024-04-10',
            'start_time': '10:00:00',
            'end_time': '11:00:00',
            'location': 'Test Location',
            'description': 'Test Description',
            'recurrence': 'monthly',
            'invited_emails': 'test1@example.com, test2@example.com'
        }

    def test_create_event(self):
        # one-time event
        response = self.client.post(reverse('create_event'), self.event_data)
        print("Response status code:", response.status_code)
        print("Event count:", Event.objects.count())
        self.assertEqual(response.status_code, 302)


    def test_monthly_event_recurrence(self):
        # monthly event
        event = Event.objects.create(
            title='Test Monthly Event',
            date=datetime.today().strftime('%Y-%m-%d'),
            start_time='10:00:00',
            end_time='11:00:00',
            location='Test Location',
            description='Test Description',
            recurrence='monthly',
            creator=self.user
        )

        next_month_date = datetime.strptime(event.date, '%Y-%m-%d') + relativedelta(months=1)
        self.client.post(reverse('create_event'), self.event_data)
        self.assertEqual(Event.objects.count(), 1)

        while next_month_date < datetime.today():
            self.assertTrue(Event.objects.filter(date=next_month_date.strftime('%Y-%m-%d')).exists())
            next_month_date += relativedelta(months=1)

