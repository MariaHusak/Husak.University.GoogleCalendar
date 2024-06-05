import os
import django
from datetime import datetime, timedelta
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from main.models import Event
from main.views import display_calendar
from unittest.mock import patch, MagicMock

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycalendar.settings')
django.setup()

class CalendarCategoriesTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='password')

    @patch('main.views.render')
    def test_display_calendar(self, mock_render):
        event1 = Event.objects.create(title='Event 1', date=datetime.today().date(), start_time='10:00:00',
                                      end_time='12:00:00', category='work', creator=self.user)
        event2 = Event.objects.create(title='Event 2', date=datetime.today().date(), start_time='14:00:00',
                                      end_time='16:00:00', category='personal', creator=self.user)
        event3 = Event.objects.create(title='Event 3', date=datetime.today().date(), start_time='18:00:00',
                                      end_time='20:00:00', category='social', creator=self.user)

        request = self.factory.get(reverse('calendar'))
        request.user = self.user

        mock_response = MagicMock()
        mock_response.content = f"{event1.title}, {event2.title}, {event3.title}".encode()
        mock_render.return_value = mock_response

        response = display_calendar(request)

        self.assertEqual(mock_render.call_count, 1)

        self.assertIn(event1.title.encode(), response.content)
        self.assertIn(event2.title.encode(), response.content)
        self.assertIn(event3.title.encode(), response.content)

