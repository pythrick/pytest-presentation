def test_value_in_list():
    assert 1 in [1, 2, 3, 4, 5], "1 should be in list"


def test_compare_sizes():
    assert 3 < 4, "3 should be lower than 4"


def test_string_contains_in_another_string():
    assert "fiz" in "fizzbuzz", "Fiz should be in fizzbuzz"


def test_sum_two_numbers():
    assert 234 + 234 == 468
