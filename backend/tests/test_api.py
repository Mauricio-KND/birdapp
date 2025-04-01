import os
from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)

def test_identify_bird_success():
    test_audio = os.path.join(os.path.dirname(__file__), "test_data", "bird_sample.mp3")
    with open(test_audio, "rb") as f:
        response = client.post(
            "/identify-bird/",
            files={"audio": ("bird_sample.mp3", f, "audio/mpeg")}
        )
    assert response.status_code == 200
    assert "Erithacus rubecula" in response.json()["species"]

def test_identify_bird_invalid_file():
    response = client.post(
        "/identify-bird/",
        files={"audio": ("test.txt", b"not an audio file", "text/plain")}
    )
    assert response.status_code == 400  # Expect 400, not 500