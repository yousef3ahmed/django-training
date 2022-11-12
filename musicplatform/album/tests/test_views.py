import pytest
from collections import OrderedDict


@pytest.mark.django_db
def test_create_album( auth_client , artists ):
    album = {
        "name": "i am test",
        "release": "2022-11-10",
        "cost": '234.23'
    }
    response = auth_client.post('http://127.0.0.1:8000/album/apiAlbums/',album)
    assert response.status_code == 200 
    assert response.data == {
         "name": "i am test",
         "release": "2022-11-10T00:00:00Z",
         "cost": '234.23'
    }

@pytest.mark.django_db
def test_user_create_album(user  , auth_client): # normal user is not artist, so not accept this
    album = {
        "name": "i am test",
        "release": "2022-11-10",
        "cost": '234.23'
    }
    response = auth_client.post('http://127.0.0.1:8000/album/apiAlbums/',album)
    assert response.status_code == 403


@pytest.mark.django_db
def test_unauthenticated_create_album(Client , artists ):
    album = {
        "name": "i am test",
        "release": "2022-11-10",
        "cost": '234.23'
    }
    response = Client.post('http://127.0.0.1:8000/album/apiAlbums/',album)
    assert response.status_code == 403

@pytest.mark.django_db
def test_get_albums(Client , album ):
    response = Client.get('http://127.0.0.1:8000/album/apiAlbums/')
    assert response.data == [OrderedDict([('id', 1), ('artist', OrderedDict([('id', 1), ('Stage', 'Yousef_pop'), ('Social_link', 'https://www.instagram.com/yousef_amers/'), ('user', 1)])), ('name', 'i am test__'), ('release', '2022-11-10T00:00:00Z'), ('cost', '234.23')])]
