import pytest



@pytest.mark.django_db
def  test_user_registration( client ):    
    response = client.post('http://127.0.0.1:8000/authentication/api_register',json={
        "username" : "yousef3ahmed",
        "email" : "activedade@gmail.com",
        "password1" : "adwmfqwpfqmpfqwf343A",
        "password2" : "adwmfqwpfqmpfqwf343A"
    })
    assert response.status_code == 201


@pytest.mark.django_db
def test_unAuthenticated_not_match_password( client ):    

    # failed because not match password

    response = client.post('http://127.0.0.1:8000/authentication/api_register',json={
        "username" : "yousef3ahmed",
        "email" : "activedade@gmail.com",
        "password1" : "adwmfqwpfqmpfqwf343AYY",
        "password2" : "adwmfqwpfqmpfqwf343A"
    })
    assert response.status_code == 400



@pytest.mark.django_db
def test_unAuthenticated_forget_username( client ):    

    # failed because not match password

    response = client.post('http://127.0.0.1:8000/authentication/api_register',json={
        "email" : "activedade@gmail.com",
        "password1" : "adwmfqwpfqmpfqwf343AYY",
        "password2" : "adwmfqwpfqmpfqwf343A"
    })
    assert response.status_code == 400

@pytest.mark.django_db
def test_login( client , user ):
    
    response = client.post('http://127.0.0.1:8000/authentication/api_login', json = {
        "username" : "YousefAhmed",
        "password" : "root"
    })

    assert response.status_code == 200

@pytest.mark.django_db
def test_login_not_exist( client ):
    
    response = client.post('http://127.0.0.1:8000/authentication/api_login', json = {
        "username" : "YousefAhmed",
        "password" : "rootttttt"
    })

    assert response.status_code == 400


@pytest.mark.django_db
def test_logout( client , auth_client  ):
    
    # login first.
    client.post('http://127.0.0.1:8000/authentication/api_login', json = {
        "username" : "YousefAhmed",
        "password" : "root"
    })
    response = auth_client.post('http://127.0.0.1:8000/authentication/api_logout' )

    assert response.status_code == 200

