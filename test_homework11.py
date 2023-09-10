from homework11 import get_numbers
import pytest

def test_negative_age():
    assert get_numbers(-5) == "an invalid age value was passed because age cannot be less than 0"

def test_child_age():
    assert get_numbers(5) == "You are baby"
    assert get_numbers(18) == "You are baby"

def test_working_age():
    assert get_numbers(25) == "You have to work"
    assert get_numbers(65) == "You have to work"

def test_retirement_age():
    assert get_numbers(70) == "Happy retirement"
