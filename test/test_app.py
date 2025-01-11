import pytest
from app.app import add, subtract, multiply, divide


def test_add():
    """Тестирует функцию сложения."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Тестирует функцию вычитания"""
    assert subtract(10, 5) == 5
    assert subtract(6,3) == 3

def test_multiply():
    """Тестирует функцию умножения"""
    assert multiply(5,5) == 25
    assert multiply(10,10) == 100


def test_divide():
    """Тестирует функцию деления."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    with pytest.raises(ValueError):
        divide(5, 0)
