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


@pytest.fixture
def get_client(user):
    def api_client( user_instance = None ):
        
        if user_instance is None:  
            client = APIClient()  
            response = client.post('http://127.0.0.1:8000/authentication/api_login', json = {
                "username" : "YousefAhmed",
                "password" : "root"
            })
            token = response.data["token"]
            print( token )
            client.credentials(HTTP_AUTHORIZATION='Token ' + token)
            return client
        else:
            client = APIClient()
            random_user = User.objects.create_user(user_instance['username'], user_instance['email'], user_instance['password'])
            login= client.post('http://127.0.0.1:8000/authentication/api_login', 
            dict( username=user_instance["username"], 
                  password = user_instance["password"]) )
            token = response.data["token"]
            client.credentials(HTTP_AUTHORIZATION='Token ' + token)
            return client
    
    return api_client





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




