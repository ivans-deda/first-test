import pytest

# Arrange-Act-Assert pattern for FastAPI endpoints

def test_list_activities(client):
    # Arrange
    # (client fixture provides TestClient)
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_signup_activity(client):
    # Arrange
    activity = "Chess Club"
    email = "student1@mergington.edu"
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert response.status_code == 200
    assert "message" in response.json()


def test_prevent_duplicate_signup(client):
    # Arrange
    activity = "Chess Club"
    email = "student2@mergington.edu"
    client.post(f"/activities/{activity}/signup?email={email}")
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up"


def test_unregister_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "student3@mergington.edu"
    client.post(f"/activities/{activity}/signup?email={email}")
    # Act
    response = client.post(f"/activities/{activity}/unregister?email={email}")
    # Assert
    assert response.status_code == 200
    assert "message" in response.json()


def test_invalid_activity_signup(client):
    # Arrange
    activity = "Nonexistent Activity"
    email = "student4@mergington.edu"
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
