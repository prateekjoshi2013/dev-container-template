
def test_read_main_client(test_client):
    item_id=10
    response = test_client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"item_id": 10}
