def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"You are at home" in response.data


def test_sign_in(client):

    # bug: sign-in :: not sign_in
    response = client.get("/sign_in")

    assert response.status_code == 200
    assert b"Sign In Page" in response.data
