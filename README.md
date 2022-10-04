
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
## create some albums and assign them to any artists.
```
>>> p = Album( artist = Artist.objects.get(pk=1) , pub_date = timezone.now() , release = timezone.now() , cost = '167.86')
>>> p.save()
```
## get all albums released today or before but not after today.
```
>>> records = []
>>> for e in Album.objects.all():
...     if e.was_released_today_or_before():
...             records.append( e )
... 
>>> print(records) 
[<Album: Name = New Album --- Artist = yousef>, <Album: Name = New Album --- Artist = yousef>]
```

## get all albums released before today
```
>>> records = []
>>> 
>>> for e in Album.objects.all():
...     if e.was_released_before_today():
...             records.append( e )
... 
>>> print( records  ) 
[]
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


