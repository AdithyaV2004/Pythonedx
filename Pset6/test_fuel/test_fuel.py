# test_fuel.py
import pytest
from fuel import convert, gauge

def test_convert_normal():
    assert convert("1/2") == "50%"
    assert convert("3/4") == "75%"
    assert convert("1/4") == "25%"
    assert convert("99/100") == "F"
    assert convert("1/100") == "E"

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_invalid_fraction():
    with pytest.raises(ValueError):
        convert("3/2")  # num > den is not allowed
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
