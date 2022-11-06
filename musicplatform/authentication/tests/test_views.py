import pytest



@pytest.mark.django_db
def test_unAuthenticated( client ):    
    response = client.post('http://127.0.0.1:8000/authentication/api_register',json={
         "username" : "MegaCoredadp",
        "email" : "activedade@gmail.com",
        "password1" : "adwmfqwpfqmpfqwf343A",
        "password2" : "adwmfqwpfqmpfqwf343A"
    })
    assert response.status_code == 201


