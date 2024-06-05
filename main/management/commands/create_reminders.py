from datetime import datetime
from main.models import Event
from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Send reminders for upcoming events'

    def handle(self, *args, **kwargs):
        today = datetime.now()

        for user in User.objects.all():
            upcoming_events = user.created_events.filter(date__gte=today.date())

            for event in upcoming_events:
                time_until_event = datetime.combine(event.date, event.start_time) - today

                if time_until_event.days == 0:
                    try:
                        send_mail(
                            'Upcoming Event Reminder',
                            f'Don\'t forget! You have an event "{event.title}" scheduled for {event.date} at {event.start_time}.',
                            'husakmaria74@email.com',
                            [event.creator.email],
                            fail_silently=False,
                        )
                        self.stdout.write(self.style.SUCCESS(f'Reminder sent for event "{event.title}" to user "{event.creator.username}"'))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Failed to send reminder for event "{event.title}": {e}'))


        if not User.objects.filter(created_events__date__gte=today.date()).exists():
            raise CommandError('No upcoming events found for any user')

