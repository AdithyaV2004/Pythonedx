import pytest

from bank import value

def test_hello():
    assert value("Hello") == 0

def test_h():
    assert value("Howdy") == 20

def test_greetings():
    assert value("Surprise, Motherfucker")== 100


