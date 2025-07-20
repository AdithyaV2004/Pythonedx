import pytest
from twttr import shorten

def test_shorten():
    assert shorten("Adithya")=="dthy"
    assert shorten("qwrtyp")=="qwrtyp"

def test_number():
    assert shorten("123456")=="123456"

def test_alphanum():
    assert shorten("Adi123thya456")=="d123thy456"

def test_punctuation():
    assert shorten("Adithya!.")=="dthy!."
