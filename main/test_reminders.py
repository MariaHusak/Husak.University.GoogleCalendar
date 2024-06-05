import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycalendar.settings')
django.setup()

import unittest
from unittest.mock import patch, MagicMock
from crontab import CronTab

def create_reminder_job():
    job_scheduler = CronTab(user=True)
    command = 'python3 ./manage.py create_reminders'
    job = job_scheduler.new(command=command)
    job.minute.on(0)
    job.hour.on(0)
    return job

class TestCronJob(unittest.TestCase):
    @patch('crontab.CronTab')
    def test_cron_job_setup(self, mock_crontab):
        mock_job = MagicMock()

        mock_crontab_instance = MagicMock()
        mock_crontab_instance.new.return_value = mock_job
        mock_crontab.return_value = mock_crontab_instance

        create_reminder_job()

        mock_crontab_instance(command='python3 ./manage.py create_reminders')

        mock_job.minute.on(0)
        mock_job.hour.on(0)
