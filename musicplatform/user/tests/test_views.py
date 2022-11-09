import pytest
from rest_framework.test import RequestsClient
from django.contrib.auth import get_user_model
from knox.models import AuthToken
from rest_framework.test import force_authenticate




def test_GET_User( user, auth_client ):
    response = auth_client.get("http://127.0.0.1:8000/user/api_detail/1")
    
    assert response.data == { "email":"email.com",
                               'id': 1, 
                               'username': 'YousefAhmed',
                                'bio' : ''
                                }


def test_get_wrong_id( user, auth_client ):
    response = auth_client.get('http://127.0.0.1:8000/user/api_detail/1000')
    assert response.status_code == 404


def test_update_put( auth_client  , user ):
    
 
    update_data  = {
         "bio" : "i am test now the updatesss.",
         "username" : "yousef14ahmed",
         "email":"yousef.amer5@gmail.bld.ai",
         "password" :"youssef_____"
    }

    response = auth_client.put( f'/user/api_detail/{user.id}', update_data )
    
    assert response.data == {"bio" : "i am test now the updatesss.",
                             "email":"yousef.amer5@gmail.bld.ai",
                             'id': 1, 
                             'username': 'yousef14ahmed'}


def test_update_put_err( auth_client  , user ):
    
    update_data  = {
         "bio" : "i am test now the updatesss.",
         "email":"yousef.amer5@gmail.bld.ai",
         "password" :"youssef_____"
    }

    response = auth_client.put( f'/user/api_detail/{user.id}', update_data )
    assert response.status_code == 400


def test_update_patch( auth_client  , user  ):
    
    update_data  = {
         "bio" : "i am test now the updatesss.",
         "username" : "yousef14ahmed"
    }

    response = auth_client.put( f'/user/api_detail/{user.id}', update_data )
   
    assert response.data == {'bio': 'i am test now the updatesss.', 
                             'email': 'email.com', 
                             'id': 1, 
                             'username': 'yousef14ahmed'}