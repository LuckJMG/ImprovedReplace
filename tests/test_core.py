#!/usr/bin/python3
from improved_replace.core import *

def test_to_array():
    """Test to_array function."""

    # Normal string
    assert to_array("Hello World") == ["Hello", "World"]

    # Many spaces
    assert to_array(" H e l l o ") == ["H", "e", "l", "l", "o"]

    # Only spaces
    assert to_array("           ") == []

    # Any spaces
    assert to_array("HelloWorld!") == ["HelloWorld!"]

    # Not a string
    assert to_array(None) == None


def test_to_point():
    """Test to_point function."""

    # Normal string
    assert to_point("Hello World,") == "Hello World."

    # Many commas
    assert to_point(",,,,,.,,,,,,") == "............"

    # Any commas
    assert to_point("            ") == "            "

    # Not a string
    assert to_point(1225) == 1225


def test_to_comma():
    """Test to_comma function."""

    # Normal string
    assert to_comma("Hello. World") == "Hello, World"

    # Many points
    assert to_comma(".....,......") == ",,,,,,,,,,,,"

    # Any points
    assert to_comma("            ") == "            "

    # Not a string
    assert to_point(12.25) == 12.25
