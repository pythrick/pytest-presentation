import os

import pytest


@pytest.fixture
def tasks():
    return ["Buy coffee", "Drink water", "Listen music"]


@pytest.fixture
def temp_file():
    file_name = "temp_file.txt"
    with open(file_name, "w") as f:
        f.write("testing file...")
    yield file_name
    os.remove(file_name)



@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    """Remove requests.sessions.Session.request for all tests."""
    monkeypatch.delattr("requests.sessions.Session.request")
