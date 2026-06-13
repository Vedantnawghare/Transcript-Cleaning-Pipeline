from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)



def test_clean_api():

    response = client.post(
        "/clean",
        json={
            "text":
            "umm i worked on python and docker"
        }
    )


    assert response.status_code == 200

    assert response.json()["cleaned"] == \
        "I worked on Python and Docker."



def test_empty_text():

    response = client.post(
        "/clean",
        json={
            "text":""
        }
    )


    assert response.status_code == 422