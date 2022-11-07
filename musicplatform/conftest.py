import pytest
from rest_framework.test import APIClient
from rest_framework.test import RequestsClient
from knox.models import AuthToken
from user.models import User
from artists.models import Artist
from album.models import Album


@pytest.fixture()
def artists(db):
    artists = Artist.objects.create(
        Stage = 'Yousef_pop',
        Social_link = 'https://www.instagram.com/yousef_amers/'
    )

@pytest.fixture()
def user(db):
    user = User.objects.create_user(  email='email.com',
                                      username='YousefAhmed',
                                      password = 'root' )
    return user




@pytest.fixture()
def auth_client(user):
    client = APIClient()
    _, token = AuthToken.objects.create(user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    return client



@pytest.fixture
def client():
    return RequestsClient()

@pytest.fixture
def Client():
    return APIClient()




