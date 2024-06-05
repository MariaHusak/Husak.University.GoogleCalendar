import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycalendar.settings')
django.setup()


from django.test import TestCase, Client
from unittest.mock import patch
from .models import Event, User
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Unit testing for Event Creation endpoints
"""class EventCreationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        self.invited_user = User.objects.create_user(username='inviteduser', email='inviteduser@example.com', password='password')
        self.client.login(username='testuser', password='password')

    @patch('main.views.send_mail')
    def test_create_event(self, mock_send_mail):
        data = {
            'event_title': 'Test Event',
            'event_date': '2024-04-10',
            'start_time': '12:00',
            'end_time': '13:00',
            'event_location': 'Test Location',
            'event_description': 'Test Description',
            'invited_emails': ['inviteduser@example.com'],
            'recurrence': 'daily'
        }

        response = self.client.post(reverse('create_event'), data=data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])

        self.assertTrue(Event.objects.filter(title='Test Event').exists())

        mock_send_mail.assert_called()
        self.assertTrue(mock_send_mail.call_count >= 1)

    def test_create_event_missing_data(self):
        incomplete_event_data = {
            'event_date': '2024-04-10',
            'start_time': '12:00',
            'end_time': '13:00',
            'event_location': 'Test Location',
            'event_description': 'Test Description',
            'invited_emails': ['inviteduser@example.com'],
            'recurrence': 'daily'
        }

        response = self.client.post(reverse('create_event'), data=incomplete_event_data)

        self.assertEqual(response.status_code, 400)

        event = Event.objects.filter(title='Test Event').first()
        self.assertIsNone(event)

    def test_create_event_invalid_date(self):
        invalid_date_event_data = {
            'event_date': 'invalid-date',
            'start_time': '12:00',
            'end_time': '13:00',
            'event_location': 'Test Location',
            'event_description': 'Test Description',
            'invited_emails': ['inviteduser@example.com'],
            'recurrence': 'daily'
        }
        response = self.client.post(reverse('create_event'), data=invalid_date_event_data)

        self.assertEqual(response.status_code, 400)

        event = Event.objects.filter(title='Test Event').first()
        self.assertIsNone(event)"""


#Unit Tests for Event Creation functionality
class EventCreationFunctionalityTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_event_creation(self):
        event_data = {
            'event_title': 'Test Event',
            'event_date': '2024-04-10',
            'start_time': '10:00',
            'end_time': '12:00',
            'event_location': 'Test Location',
            'event_description': 'Test Description',
            'recurrence': None,
            'invited_emails': []
        }

        self.create_event(event_data)
        self.assertTrue(Event.objects.filter(title='Test Event').exists())


    def create_event(self, event_data):
        event_title = event_data['event_title']
        event_date = event_data['event_date']
        start_time = event_data['start_time']
        end_time = event_data['end_time']
        event_location = event_data['event_location']
        event_description = event_data['event_description']
        recurrence = event_data['recurrence']

        event = Event.objects.create(title=event_title, date=event_date, start_time=start_time,
                                     end_time=end_time, location=event_location, description=event_description,
                                     creator=self.user, recurrence=recurrence)

        invited_emails = event_data['invited_emails']
        for email in invited_emails:
            invited_user = User.objects.get(email=email)
            event.invited_users.add(invited_user)

#Unit Tests for User Authentication
class UserAuthenticationTestCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_correct_credentials(self):
        user = authenticate(username=self.username, password=self.password)
        self.assertIsNotNone(user)
        self.assertEqual(user, self.user)

    def test_incorrect_username(self):
        user = authenticate(username='wrongusername', password=self.password)
        self.assertIsNone(user)

    def test_incorrect_password(self):
        user = authenticate(username=self.username, password='wrongpassword')
        self.assertIsNone(user)

    def test_blank_credentials(self):
        user = authenticate(username='', password='')
        self.assertIsNone(user)

    def test_inactive_user(self):
        self.user.is_active = False
        self.user.save()
        user = authenticate(username=self.username, password=self.password)
        self.assertIsNone(user)


class InvalidURLTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.event = Event.objects.create(
            title='Test Event', date='2023-01-01', start_time='12:00',
            end_time='13:00', location='Test Location', description='Test Description',
            creator=self.user
        )

    def test_access_non_existent_event(self):
        response = self.client.get(reverse('edit_event', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_invalid_url(self):
        response = self.client.get('/invalid-url/')
        self.assertEqual(response.status_code, 404)

