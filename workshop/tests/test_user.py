user = {
    "username": "Darth Vader",
    "email": "vader@deathstar.com",
    "password": "rainbow"
}

user2 = {
    "username": "Petr",
    "email": "vdfh@deathstar.com",
    "password": "123"
}


def test_main_page(client):
    responce = client.get("/")
    assert responce.status_code == 404
    assert responce.json() == {"detail": "Not Found"}


def test_get_user_list(client, temp_db):
    response = client.get("/user-list/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_user_list_with_users(client, temp_db):
    response1 = client.post("/user/", json=user)
    response2 = client.post("/user/", json=user2)
    response = client.get("/user-list/")
    assert response.status_code == 200
    assert response.json()[0]["email"] == "vader@deathstar.com"
    assert response.json()[1]["email"] == "vdfh@deathstar.com"
    assert response.json()[0]["username"] == "Darth Vader"
    assert response.json()[1]["username"] == "Petr"


def test_get_user(client, temp_db):
    response1 = client.post("/user/", json=user)
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json()["email"] == "vader@deathstar.com"

def test_get_user(client, temp_db):
    response = client.get("/user/99")
    assert response.status_code == 400
    assert response.json() == {"detail": "The user does not exist"}


def test_add_user(client, temp_db):
    response = client.post("/user/", json=user)
    assert response.status_code == 201
    assert response.json()["email"] == "vader@deathstar.com"
    assert response.json()["username"] == "Darth Vader"
    assert response.json()["id"] == 1


def test_add_user_twice(client, temp_db):
    response1 = client.post("/user/", json=user)
    response2 = client.post("/user/", json=user)
    assert response2.json() == {"detail": "The user already exists"}


def test_put_user_without_json(client, temp_db):
    response = client.put("/user/99")
    assert response.status_code == 422


def test_put_user(client, temp_db):
    response1 = client.post("/user/", json=user)
    response = client.put("/user/1", json=user)
    assert response.status_code == 200
    assert response.json()["email"] == "vader@deathstar.com"
    assert response.json()["username"] == "Darth Vader"


def test_patch_user(client, temp_db):
    response1 = client.post("/user/", json=user)
    response = client.patch("/user/1", json={"username": "Hello"})
    assert response.status_code == 200
    assert response.json()["username"] == "Hello"


def test_patch_user_without_json(client, temp_db):
    response = client.patch("/user/1")
    assert response.status_code == 422
