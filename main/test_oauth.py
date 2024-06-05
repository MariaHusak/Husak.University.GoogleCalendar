import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycalendar.settings')
django.setup()


import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from faker import Faker
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

#Unit testing for OAuth endpoints

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def fake():
    return Faker()

@pytest.fixture
def social_app():
    site = Site.objects.get_current()
    social_app = SocialApp.objects.create(provider='google',
                                          name='Google',
                                          client_id='1043010912649-6vj29gm4kiaslniq4h5bfemvheg862is.apps.googleusercontent.com',
                                          secret='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')
    social_app.sites.set([site])
    return social_app

@pytest.mark.django_db
def test_oauth_login(api_client, fake, social_app):
    username = fake.user_name()
    user = User.objects.create_user(username=username, password='testpassword')
    api_client.force_authenticate(user=user)

    response = api_client.post(reverse('account_login'))

    assert response.status_code == 200

@pytest.mark.django_db
def test_oauth_logout(api_client, fake):
    username = fake.user_name()
    user = User.objects.create_user(username=username, password='testpassword')
    api_client.force_authenticate(user=user)

    response = api_client.post(reverse('account_logout'))

    assert response.status_code == 302

