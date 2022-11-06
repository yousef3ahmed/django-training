import pytest
from rest_framework.test import RequestsClient
from django.contrib.auth import get_user_model
from knox.models import AuthToken



def test_GET_User( user, auth_client ):
    response = auth_client.get(f'/user/api_detail/1')
    assert response.status_code == 200





