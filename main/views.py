import calendar
from datetime import datetime, timedelta
from django.http import JsonResponse, HttpResponse
from .models import Event
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from .forms import EventForm
from django.utils.dateparse import parse_date
from dateutil.relativedelta import relativedelta
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@login_required
def index(request):
    return render(request, 'main/index.html')

def privacy(request):
    return render(request, 'main/privacy.html')

def login(request):
    return render(request, 'account/login.html')


@login_required
def display_calendar(request, year=None, month=None):
    today = datetime.today()
    if year is None:
        year = today.year
    if month is None:
        month = today.month

    cal = calendar.Calendar()
    cal_data = cal.monthdayscalendar(year, month)

    month_name = calendar.month_name[month]
    year_name = str(year)

    next_month = (today.replace(year=year, month=month) + timedelta(days=31)).strftime('%Y/%m')
    prev_month = (today.replace(year=year, month=month) - timedelta(days=1)).strftime('%Y/%m')

    if month == 1:
        prev_month = f"{year - 1}/12"
    else:
        prev_month = f"{year}/{month - 1:02d}"

    user = request.user
    creator_events = Event.objects.filter(date__year=year, date__month=month, creator=user)
    invited_events = Event.objects.filter(date__year=year, date__month=month, attendees=user, invited_users=user)
    all_events = creator_events | invited_events

    event_data = []
    for event in all_events:
        event_info = {
            'id': event.id,
            'title': event.title,
            'date': event.date,
            'start_time': event.start_time,
            'end_time': event.end_time,
            'location': event.location,
            'category': event.category,
            'description': event.description,
            'creator_nickname': event.creator.username,
            'invited_users_nicknames': [user.username for user in event.invited_users.all()]
        }
        event_data.append(event_info)

    return render(request, 'main/calendar.html', {'calendar': cal_data, 'month_name': month_name,
                                                  'year_name': year_name, 'next_month': next_month,
                                                  'prev_month': prev_month, 'events': event_data})

@login_required
def create_event(request):
    if request.method == 'POST':
        event_title = request.POST.get('event_title')
        event_date = request.POST.get('event_date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        event_location = request.POST.get('event_location')
        event_description = request.POST.get('event_description')
        invited_emails = request.POST.getlist('invited_emails')
        recurrence = request.POST.get('recurrence')
        event_category = request.POST.get('event_category')

        creator = request.user

        if not all([event_title, event_date, start_time, end_time]):
            return JsonResponse({'success': False, 'error': 'Incomplete event data'}, status=400)

        try:
            event = Event.objects.create(
                title=event_title, date=event_date, start_time=start_time,
                end_time=end_time, location=event_location, description=event_description,
                creator=creator, recurrence=recurrence, category=event_category
            )

            if recurrence:
                if recurrence in ['daily', 'weekly', 'monthly', 'yearly']:
                    delta = None
                    if recurrence == 'daily':
                        delta = relativedelta(days=1)
                    elif recurrence == 'weekly':
                        delta = relativedelta(weeks=1)
                    elif recurrence == 'monthly':
                        delta = relativedelta(months=1)
                    elif recurrence == 'yearly':
                        delta = relativedelta(years=1)

                    if delta:
                        end_date = parse_date(event_date) + relativedelta(years=1)
                        current_date = parse_date(event_date) + delta
                        while current_date <= end_date:
                            Event.objects.create(
                                title=event_title, date=current_date, start_time=start_time,
                                end_time=end_time, location=event_location, description=event_description,
                                creator=creator, recurrence=recurrence, category=event_category
                            )
                            current_date += delta

            for email in invited_emails:
                try:
                    invited_user = User.objects.get(email=email)
                    event.invited_users.add(invited_user)

                    send_mail(
                        'You have been invited to an event',
                        f'You have been invited to the event "{event.title}" scheduled on {event_date} {start_time} - {end_time} by {creator}.',
                        'husakmaria74@gmail.com',
                        [email],
                        fail_silently=False,
                    )
                    logger.info(f'Invitation email sent to {email} for event "{event.title}"')
                except User.DoesNotExist:
                    logger.warning(f'User with email {email} does not exist. Invitation email not sent.')
                except BadHeaderError:
                    logger.error(f'Invalid header found while sending email to {email}.')
                except ValidationError as e:
                    logger.error(f'Validation error occurred while sending email to {email}: {str(e)}')

            return redirect('calendar')
        except ValidationError as ve:
            logger.error(f'Validation error while creating event: {str(ve)}')
            return JsonResponse({'success': False, 'error': ve.message_dict}, status=400)
        except Exception as e:
            logger.error(f'Failed to create event: {str(e)}')
            return JsonResponse({'success': False, 'error': 'Failed to create event'}, status=500)
    else:
        form = EventForm()
        return render(request, 'main/create_event.html', {'form': form})


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('calendar')
    else:
        form = EventForm(instance=event)
    return render(request, 'main/edit_event.html', {'form': form, 'event_id': event_id})


@login_required
def invitations_page(request):
    user = request.user
    invited_events = Event.objects.filter(invited_users=user)

    return render(request, 'main/invitations.html', {'invited_events': invited_events})


@login_required
def respond_invitation(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    response = request.POST.get('response')

    if response == 'accepted':
        event.attendees.add(request.user)
        event.save()

        send_mail(
            'Invitation Accepted',
            f'{request.user.username} has accepted your invitation to the event "{event.title}".',
            'organizer@example.com',
            [event.creator.email],
            fail_silently=False,
        )

    elif response == 'declined':
        event.invited_users.remove(request.user)
        event.save()

        send_mail(
            'Invitation Declined',
            f'{request.user.username} has declined your invitation to the event "{event.title}".',
            'organizer@example.com',
            [event.creator.email],
            fail_silently=False,
        )

    return redirect('calendar')

def search_events(request):
    query = request.GET.get('query', '')
    matched_events = []

    logger = logging.getLogger(__name__)

    if query:
        logger.info(f"Search query: {query}")

        matched_events = Event.objects.filter(
            title__icontains=query
        ).distinct()

    return render(request, 'main/search.html', {'events': matched_events})


def search_suggestions(request):
    query = request.GET.get('query', '')

    if query:
        suggestions = Event.objects.filter(title__icontains=query)
        suggestions_data = [{
            'title': suggestion.title,
            'start_time': suggestion.start_time,
            'end_time': suggestion.end_time,
            'location': suggestion.location,
            'description': suggestion.description
        } for suggestion in suggestions[:10]]
        return JsonResponse(suggestions_data, safe=False)
    else:
        return JsonResponse([], safe=False)

@receiver(user_logged_in)
def send_welcome_email(sender, user, request, **kwargs):
        send_mail(
            'Welcome to Mary Calendar',
            f'Hello {user.username},\n\nWelcome to Mary Calendar! We are excited to see you. If you have any questions or need assistance, feel free to reach out to our support team.\n\nBest regards,\nThe Team',
            'husakmaria74@gmail.com',
            [user.email],
            fail_silently=False,
        )