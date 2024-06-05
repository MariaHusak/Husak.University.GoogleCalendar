import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycalendar.settings')
django.setup()


from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail
from main.models import Event
from main.views import respond_invitation
from datetime import datetime, timedelta, date
from unittest.mock import patch

#Write Unit Tests for Guest RSVP functionality
class RespondInvitationTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.creator = User.objects.create_user(username='creator', password='password')

        start_time = datetime.now() + timedelta(hours=1)
        end_time = start_time + timedelta(hours=1)

        self.event = Event.objects.create(
            title='Test Event',
            creator=self.creator,
            date=start_time.date(),
            start_time=start_time.time(),
            end_time=end_time.time()
        )
        self.event.invited_users.add(self.user)
        self.event.save()

    @patch('main.views.send_mail')
    def test_accept_invitation(self, mock_send_mail):
        url = reverse('respond_invitation', kwargs={'event_id': self.event.pk})
        request = self.factory.post(url, {'response': 'accepted'})
        request.user = self.user

        response = respond_invitation(request, event_id=self.event.pk)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.event.attendees.filter(pk=self.user.pk).exists())
        self.assertEqual(len(mock_send_mail.call_args_list), 1)


    @patch('main.views.send_mail')
    def test_decline_invitation(self, mock_send_mail):
        url = reverse('respond_invitation', kwargs={'event_id': self.event.pk})
        request = self.factory.post(url, {'response': 'declined'})
        request.user = self.user

        response = respond_invitation(request, event_id=self.event.pk)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            self.event.invited_users.filter(pk=self.user.pk).exists())
        self.assertEqual(len(mock_send_mail.call_args_list), 1)

#Conduct unit testing for Guest RSVP endpoints
class RSVPTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.event = Event.objects.create(
            title='Test Event',
            date=date.today(),
            start_time='12:00:00',
            end_time='14:00:00',
            creator=self.user
        )
        self.client = Client()


    def test_invitations_page_unauthenticated(self):
        response = self.client.get(reverse('invitations_page'))
        self.assertEqual(response.status_code, 302)

    def test_respond_invitation_invalid_response(self):
        response = self.client.post(reverse('respond_invitation', args=[self.event.id]), {'response': 'invalid'})
        self.assertEqual(response.status_code, 302)

    def test_respond_invitation_invalid_event_id(self):
        response = self.client.post(reverse('respond_invitation', args=[999]), {'response': 'accepted'})
        self.assertEqual(response.status_code, 302)