#!/usr/bin/python3
from .context import ImprovedReplace
import pytest

# Class to test
test = ImprovedReplace()

# Testing class
class TestImprovedReplace():
    """Test ImprovedReplace Class.

    Test all the functions of Improved replace class.
    """

    def test_to_array(self):
        '''Test to_array function.'''
        assert test.to_array("Hello World") == ['Hello', 'World']           # Normal string
        assert test.to_array(" H e l l o ") == ['H', 'e', 'l', 'l', 'o']    # Many spaces
        assert test.to_array("           ") == []                           # Only spaces
        assert test.to_array("HelloWorld!") == ['HelloWorld!']              # Any spaces

    def test_comma_to_point(self):
        '''Test comma_to_point function.'''
        assert test.comma_to_point("Hello World,") == "Hello World."    # Normal string
        assert test.comma_to_point(",,,,,.,,,,,,") == "............"    # Many commas
        assert test.comma_to_point("            ") == "            "    # Any commas

    def test_point_to_comma(self):
        '''Test point_to_comma function.'''
        assert test.point_to_comma("Hello. World") == "Hello, World"    # Normal string
        assert test.point_to_comma(".....,......") == ",,,,,,,,,,,,"    # Many points
        assert test.point_to_comma("            ") == "            "    # Any points
