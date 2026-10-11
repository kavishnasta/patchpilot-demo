import pytest
from src.parser import parse_input

def test_parse_whitespace_input():
    assert parse_input('   ') == {}
