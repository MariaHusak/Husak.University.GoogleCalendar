import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycalendar.settings')
django.setup()


from django.test import TestCase
from django.urls import reverse
from .models import Event
import json
from django.contrib.auth.models import User
from datetime import date

class SearchSuggestionsTestCase(TestCase):
    def setUp(self):
        self.event1 = Event.objects.create(
            title="Event 1",
            date=date.today(),
            start_time="10:00:00",
            end_time="12:00:00",
            location="Location 1",
            description="Description 1",
            creator=User.objects.create(username="creator1")
        )
        self.event2 = Event.objects.create(
            title="Event 2",
            date=date.today(),
            start_time="13:00:00",
            end_time="15:00:00",
            location="Location 2",
            description="Description 2",
            creator=User.objects.create(username="creator2")
        )


    def test_search_suggestions_with_query(self):
        url = reverse('search_suggestions')
        query = 'Event 1'
        response = self.client.get(url, {'query': query})
        self.assertEqual(response.status_code, 302)
        suggestions = json.loads(response.content)
        self.assertEqual(len(suggestions), 1)
        self.assertEqual(suggestions[0]['title'], 'Event 1')

    def test_search_suggestions_without_query(self):
        url = reverse('search_suggestions')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        suggestions = json.loads(response.content)
        self.assertEqual(len(suggestions), 0)


