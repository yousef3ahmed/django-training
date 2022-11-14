from django.utils import timezone
from artists.models import Artist
from celery import shared_task 
from musicplatform.celery import app
from django.core.mail import send_mail

@shared_task()
def congratulation_email(id, name, release, cost):
    artist = Artist.objects.get(user_id = id)
    msssage = 'Album: ' + name + ', released: ' + release + 'and cost is: ' + str(cost)
    print( msssage )
    send_mail('Congratulate !', msssage, 'yousef.amer765@gmail.com', [artist.user.email], fail_silently=False,)



@app.task
def send_artist_a_reminder_email():
    print( "i am here" )
    for artist in Artist.objects.all():
        last_album = artist.album_set.all().order_by('-created').first()
        if last_album.created.date() < timezone.now() - timezone.timedelta(days=30) :
            message = 'Hi ' + artist.Stage + ' please release new albums.'
            print( message )
            send_mail('Reminder !',  message , 'yousef.amer765@gmail.com' , [artist.user.email])