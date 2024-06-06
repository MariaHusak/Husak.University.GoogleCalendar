from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail
from main.models import SharedCalendar
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycalendar.settings')
django.setup()


class ShareCalendarViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        self.other_user = User.objects.create_user(username='otheruser', email='otheruser@example.com',password='otherpass')
        self.client.login(username='testuser', password='testpass')
        self.url = reverse('share_calendar')

    def test_share_calendar_success(self):
        response = self.client.post(self.url, {'email': 'otheruser@example.com', 'can_edit': 'on'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            SharedCalendar.objects.filter(owner=self.user, shared_with=self.other_user, can_edit=True).exists())
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Calendar Sharing Request')
        self.assertIn('testuser has shared their calendar with you.', mail.outbox[0].body)
        self.assertEqual(mail.outbox[0].to, ['otheruser@example.com'])

    def test_share_calendar_user_does_not_exist(self):
        response = self.client.post(self.url, {'email': 'nonexistent@example.com', 'can_edit': 'on'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'success': False, 'error': 'User does not exist'})
        self.assertEqual(len(mail.outbox), 0)

    def test_share_calendar_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/share_calendar.html')
