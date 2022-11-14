from django.utils import timezone
from artists.models import Artist
from celery import shared_task
from django.core.mail import send_mail

@shared_task()
def send_artist_a_congratulation_email(id, album_name, release, cost):
    artist = Artist.objects.get(user_id = id)
    msssage = 'Album: ' + album_name + ', released: ' + release + 'and cost is: ' + str(cost)
    send_mail('Congratulate !', msssage, 'mahmoud.gmail.com', [artist.user.email], fail_silently=False,)

@shared_task()
def send_artist_a_reminder_email():
    for artist in Artist.objects.all():
        last_album = artist.album_set.all().order_by('-created').first()
        if last_album.created.date() < timezone.now() - timezone.timedelta(days=30):
            message = 'Hi ' + artist.Stage + ' we miss your albums, please release new albums such that people know you.'
            send_mail('Reminder !', message,'mahmoud.gmail.com', [artist.user.email])