from flask_babel import gettext



def test_create_user(client):
    data = {
        "email": "luckyluke@yahoo.com",
        "username": "luckyluke",
        "password": "luckyluke"
    }
    response = client.post('/users', json=data)
    assert '201' in response.status
    