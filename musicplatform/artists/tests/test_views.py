import pytest
from artists.models import Artist
from rest_framework.parsers import JSONParser


@pytest.mark.django_db
def test_list_artists( Client  ):
    response = Client.get('http://127.0.0.1:8000/artists/api')
    assert response.status_code == 200    


@pytest.mark.django_db
def test_create_artists( Client  ):

    post_data ={ 
                 'Stage' : 'yousef ahmed_', 
                 'Social_link' : 'https://www.facebook.com/youssef.amer.7165/' }

    response = Client.post('http://127.0.0.1:8000/artists/api' , post_data )
    assert response.data == {
        'Stage': 'yousef ahmed_',
        'Social_link' : 'https://www.facebook.com/youssef.amer.7165/'
    }

@pytest.mark.django_db
def test_create_artists_with_err( Client  ):

    post_data ={ 'Stage' : 'yousef ahmed_',
                'Social_link' : '888888' }
    response = Client.post('http://127.0.0.1:8000/artists/api' , post_data )
    assert response.status_code == 400



@pytest.mark.django_db
def test_Artist_unique_name(client , user):
    data ={ 
                 'Stage' : 'yousef ahmed_', 
                 'Social_link' : 'https://www.facebook.com/youssef.amer.7165/' }
    
    response = client.post('http://localhost:8000/artists/',data)
    response = client.post('http://localhost:8000/artists/',data)
    assert response.status_code == 403
