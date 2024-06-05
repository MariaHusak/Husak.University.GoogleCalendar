import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycalendar.settings')
django.setup()


from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.core import mail
from unittest.mock import patch
from django.contrib.auth import authenticate

#Write Unit Tests for Welcome Email
class WelcomeEmailTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password', email='testuser@example.com')

    @patch('main.views.send_mail')
    def test_welcome_email_sent_on_login(self, mock_send_mail):
        self.client.login(username='testuser', password='password')

        mock_send_mail.assert_called_once_with(
            'Welcome to Mary Calendar',
            'Hello testuser,\n\nWelcome to Mary Calendar! We are excited to see you. If you have any questions or need assistance, feel free to reach out to our support team.\n\nBest regards,\nThe Team',
            'husakmaria74@gmail.com',
            ['testuser@example.com'],
            fail_silently=False,
        )

    def test_email_content(self):
        with patch('main.views.send_mail') as mock_send_mail:
            self.client.login(username='testuser', password='password')

            email_content = f'Hello {self.user.username},\n\nWelcome to Mary Calendar! We are excited to see you. If you have any questions or need assistance, feel free to reach out to our support team.\n\nBest regards,\nThe Team'

            mock_send_mail.assert_called_once()
            args, kwargs = mock_send_mail.call_args
            self.assertEqual(args[0], 'Welcome to Mary Calendar')
            self.assertEqual(args[1], email_content)
            self.assertEqual(args[2], 'husakmaria74@gmail.com')
            self.assertEqual(args[3], [self.user.email])
            self.assertFalse(kwargs.get('fail_silently', True))

