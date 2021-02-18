import pytest


@pytest.mark.skip()
def test_subtract():
    # Arrange
    num1 = 1
    num2 = 2

    # Act
    result = num1 - num2

    # Assert
    assert result == -1
