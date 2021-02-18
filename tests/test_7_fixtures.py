"""
Test fixtures refer to the mechanism pytest
provides to allow the separation of “getting
ready for” and “cleaning up after” code from
your test functions
"""
import os

import pytest


@pytest.fixture
def some_data():
    """
    Answer to ultimate question
    :return: 42
    """
    return 42


def test_some_data(some_data):
    assert some_data == 42


def test_some_data_xpto(some_data):
    assert some_data < 100


# Take a look in tests/conftest.py file
def test_add_task(tasks):
    tasks.append("Buy a new book")
    assert len(tasks) == 4


def test_remove_task(tasks):
    tasks.pop()
    assert len(tasks) == 2


def test_temp_file(temp_file):
    assert os.path.exists(temp_file)


def test_temp_file_does_not_exist():
    assert not os.path.exists("temp_file.txt")
