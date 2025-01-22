import pytest
from app.app import divide


@pytest.mark.parametrize("a,b,expected", [(2,3,5),(-1,1,0),(0,0,0)])
def test_add(a,b,expected):
    """Тестирует функцию сложения."""
    assert a + b == expected

@pytest.mark.parametrize("a,b,expected", [(10,5,5), (6,3,3), (5,5,0)])
def test_subtract(a,b,expected):
    """Тестирует функцию вычитания"""
    assert a - b == expected

@pytest.mark.parametrize("a,b,expected", [(5,2,10), (10,10,100), (5,5,25)])
def test_multiply(a,b,expected):
    """Тестирует функцию умножения"""
    assert a * b == expected

@pytest.mark.parametrize("a,b,expected", [(100,10,10), (10,2,5), (5,0,ValueError)])
def test_divide(a,b,expected):
    """Тестирует функцию деления."""
    if b == 0:
        with pytest.raises(ValueError):
            divide(a,b)
    else:
        assert a / b == expected
