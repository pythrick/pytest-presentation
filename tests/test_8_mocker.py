import pytest
from pytest_presentation.joke import get_random_joke


def test_get_random_joke(mocker):
    class FakeResponse:
        @staticmethod
        def raise_for_status():
            return

        @staticmethod
        def json():
            return {"setup": "My custom", "punchline": "joke"}

    mocker.patch("requests.get", return_value=FakeResponse)
    joke = get_random_joke()
    assert joke == "My custom joke"


def test_get_random_joke_raising_exception(mocker):
    mocker.patch("requests.get", side_effect=Exception("Somethin wrong"))
    joke = get_random_joke()
    assert joke == "Unavailable at moment."


@pytest.mark.skip
def test_get_random_joke_without_mock():
    joke = get_random_joke()
    assert joke == "Unavailable at moment."
