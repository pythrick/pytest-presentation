import pytest


@pytest.mark.parametrize(
    ("num1", "num2", "expected_result"),
    [(1, 2, 2), (4, 2, 8), (100, 20, 2000), (123, 0, 0), (345, 124, 42780)],
)
def test_multiply(num1, num2, expected_result):
    # Act
    result = num1 * num2

    # Assert
    assert result == expected_result
