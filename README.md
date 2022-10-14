
# Getting Started with Create Django Project.

## In first import two model and timezone.
``` 
>>> from artists.models import Artist, Album
>>> from django.utils import timezone
```

## Create some artists.
```
>>> p = Artist( Stage = "youssef ahmed" , Social_link = 'https://www.instagram.com/yousef_amers/' )
>>> p.save()
```

## list down all artists.
```
>>> Artist.objects.all()
<QuerySet [<Artist: Stage = yousef --- Social = https://www.instagram.com/yousef_amers/>, <Artist: Stage = youssef ahmed --- Social = https://www.instagram.com/yousef_amers/>]>
```

## list down all artists sorted by name.
```
>>> Artist.objects.order_by('-Stage') 
<QuerySet [<Artist: Stage = youssef ahmed --- Social = https://www.instagram.com/yousef_amers/>, <Artist: Stage = yousef --- Social = https://www.instagram.com/yousef_amers/>]>
```

## list down all artists whose name starts with `a` .
```
>>> Artist.objects.filter(Stage__startswith='a')
<QuerySet []>
>>> Artist.objects.filter(Stage__startswith='y') 
<QuerySet [<Artist: Stage = yousef --- Social = https://www.instagram.com/yousef_amers/>, <Artist: Stage = youssef ahmed --- Social = https://www.instagram.com/yousef_amers/>]>
```
## in 2 different ways, create some albums and assign them to any artists.
```
>>> p = Album( artist = Artist.objects.get(pk=1) , pub_date = timezone.now() , release = timezone.now() , cost = '167.86')
>>> p.save()

------------------------------------------------------------------------------------
>>> b = Artist.objects.get( id  = 2 )
>>> album = b.album_set.create( pub_date = timezone.now() , release = timezone.now() ,  cost = '348007.86' )

```
## get all albums released today or before but not after today.
```
>>> Album.objects.filter(release__lte= timezone.now())          
<QuerySet [<Album: Name = New Album --- Artist = ali>, <Album: Name = New Album --- Artist = ali>, <Album: Name = New Album --- Artist = youssef ahmed>]>

```

## get all albums released before today
```
>>> import datetime
>>> Album.objects.filter(release__lte= timezone.now() - datetime.timedelta(days=1) )
<QuerySet [<Album: Name = New Album --- Artist = ali>]>

```
## count the total number of albums
```
>>> Album.objects.count()
2
```
## list down all albums ordered by cost then by name (cost has the higher priority).
```
>>> Album.objects.order_by('-cost' , 'name')                                                             
<QuerySet [<Album: Name = New Album --- Artist = ali>, <Album: Name = New Album --- Artist = yousef>, <Album: Name = New Album --- Artist = yousef>]>
``` 
## album name shouldn't contain inappropriate expressions
```
>>> from django.utils import timezone
>>>
>>> p = Album( artist = Artist.objects.get(pk=2) , name = "God-damned", pub_date = timezone.now() , release = timezone.now() , cost = '16877.86')
>>> p.save()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "D:\bld.ai\projects\Back_end\django_project\musicplatform\artists\models.py", line 49, in save
    raise ValidationError( "album name shouldn't contain inappropriate expressions !!" )
django.core.exceptions.ValidationError: ["album name shouldn't contain inappropriate expressions !! "]
```

