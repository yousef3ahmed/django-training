from album.serializers import AlbumSerializer , AlbumRequestSerializer
import pytest



@pytest.mark.django_db
def test_album_serializer_valid(artists , user):
    data = {
        "name": "pop" ,
        "release": "2022-07-01" ,
        "cost": '12.98',
        "artist": artists
    } 
    serializer = AlbumSerializer(data = data)
    assert serializer.is_valid()

    assert serializer.data == {
         'cost': '12.98' ,
         'release': '2022-07-01T00:00:00Z' ,
         'name' : 'pop'}


@pytest.mark.django_db
def test_album_serializer_invalid(artists ):
    data = {
        "cost": '12.98 ',
        "artist": artists
    } 
    serializer = AlbumSerializer(data = data)
    assert not serializer.is_valid()


@pytest.mark.django_db
def test_album_request_serializer_valid(artists):
    data = {
        "name": "pop" ,
        "release": "2022-07-01" ,
        "cost": '12.98',
     } 
    serializer = AlbumRequestSerializer(data=data ,context={'artist': artists})
    assert serializer.is_valid()
    assert serializer.data == {
        "name": "pop" ,
        'release': '2022-07-01T00:00:00Z' ,
        "cost": '12.98',
     } 

@pytest.mark.django_db
def test_album_request_serializer_invalid(artists):
    data = {
        "name": "pop" ,
        "release": "yousef" ,
        "cost": '12.98',
     } 
    serializer = AlbumRequestSerializer(data=data ,context={'artist': artists})
    assert not serializer.is_valid()
   
