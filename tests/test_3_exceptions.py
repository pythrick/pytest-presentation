import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert 10 / 0
