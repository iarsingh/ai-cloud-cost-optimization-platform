from fastapi.testclient import TestClient
from aicost.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'find idle disks', **{'payload': {'disks': [{'id': 'd1', 'attached': False, 'size_gb': 200}, {'id': 'd2', 'attached': True, 'size_gb': 200}]}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["idle_disks"] == ["d1"]
    refused = client.post("/agent/run", json={"goal": 'delete disk d1'}).json()
    assert refused["refused"] is True
