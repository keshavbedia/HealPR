import pytest
from calculator import add_numbers, multiply_numbers

def test_add_numbers():
    result = add_numbers(5, 3)
    assert result == 8, f"Expected 8, but got {result}"

def test_multiply_numbers():
    result = multiply_numbers(4, 3)
    assert result == 12
