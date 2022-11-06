import pytest
from rest_framework.test import APIClient
from rest_framework.test import RequestsClient
from knox.models import AuthToken
from user.models import User

@pytest.fixture()
def user(db):
    user = User.objects.create_user(  email='email.com',
                                      username='Yousef Ahmed',
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